---
aliases: []
author: Maneesh Sutar
date: 2024-05-10
tags:
- public
- linux
- container
title: Docker
---

# Docker

## Docker reliaying on containerd

See: <https://www.docker.com/blog/extending-docker-integration-with-containerd/>

See `nerdctl help` for all the things that containerd can do, compare with `docker help`

### tried and verified

Docker depends on [containerd](containerd.md) for

1. docker pull  
   Possible reason: docker pull requires creation of some overlay fs, for which docker needs containerd

1. container lifecycle management (create stop run containers)  
   of course, all docker images are also run with `containerd-shim` with some runtime like `runc`

Docker does not depend on containerd for

1. building images (docker can pull the base image required in the Dockerfile)  
   Docker version >23.0 depends on buildx tool, which in turns depends on buildkit.  
   Docker needs to installs necessary buildx and buildkit as a seperate plugin `apt install docker-buildx-plugin`  
   See the [docker build architecture](https://docs.docker.com/build/architecture/#buildx) and [buildkit](https://github.com/moby/buildkit)

containerd can also build images if `buildkit` is installed and its running as system service `buildkit`.  
Use `systemctl start buildkit` to start buildkitd daemon  
Then `nerdctl` can be used to build images from dockerfile.  
Note than images build by nerdctl, even with `--namespace moby` are not visible to the docker i.e. they won't show up when running `docker images`

1. push images  
   Docker can push local images to the dockerhub even if the containerd is not running  
   Even though docker depends on containerd for docker pull, the images are stored in seperate folders  
   docker: /var/lib/docker , and containnerd: /var/lib/containerd (i don't know the exact path, its something related to overlay-fs)

1. docker-cli commands: docker images, docker ps

### same namspace, different storage

Containerd can group images, containers and plugins into seperate "namespaces".  
For dockerd, the default namespace is "moby".  
e.g. Running `docker pull` will store the images under the "moby" namespace  
You can change the namespace of the `dockerd` with `--containerd-namespace` flag.

We know that docker relies on containerd for pulling of the image.  
But running `nerdctl --namespace moby images` does not show any pulled docker images (forget the built images)  
Additionally, if you pull an image with `nerdctl -n moby pull <image>` thus specifying "moby" as the namespace, the pulled image won't be visible with `docker images` command.

The reason is the dockerd and containerd store the images in seperate locations in filesystem.

Docker depends on containerd for container lifecycle, and `containerd` ultimately calls containerd-shim which runs the containers.  
Thus docker images too are run with containerd-shim but with the namespace of dockerd, default "moby".

 > 
 > If you check ps aux after `docker run` or `nerdctl run` you can see `/usr/bin/containerd-shim-runc-v2 -namespace moby -id <container id> -address <containerd_socket>`

Once you run a docker image using `docker run`, you can see the docker images being run as containers with `nerdctl -n moby ps`. But nerdctl still has no information regarding which image was used to run the container, and it will show empty image id. Even `nerdctl inspect` on the docker container shows no information about the image, and shows very few details like networking. The information regarding the image is isolated within the docker program.  
Additionaly, if you run a nerdctl image in moby namespace e.g. `nerdctl -n moby run <image>` , the resultant container will only be visible in `nerdctl -n moby ps` and `docker ps` will not show the container

docker vs containerd: <https://www.wallarm.com/cloud-native-products-101/containerd-vs-docker-what-is-the-difference-between-the-tools#:~:text=Containerd%20can%20replace%20Docker%2C%20but,communicate%20with%20the%20host%20operating>.

### integration with systemd

Now we well know that dockerd depends on containerd. So before dockerd process starts, the containerd process must start with the appropriate `containerd.sock` file.

In [systemd](../systemd.md) based machines, this is done using `.service` files.  
See the [docker.service](https://github.com/moby/moby/tree/master/contrib/init/systemd) and [containerd.service](https://github.com/containerd/containerd/blob/main/containerd.service)

In the `docker.service` file we can see that the docker service "wants" the containerd service. So starting docker service will always start the containerd service too.  
In the containerd service, no options are passed to `/usr/bin/containerd` executable.  
By default, `/usr/bin/containerd` will create a managed containerd socket at `/run/containerd/containerd.sock`  
Once containerd has started, the docker system service will launch `dockerd` while pointing the `--containerd` flag to the above `/run/containerd/containerd.sock` (see the docker.service).

#### But why run containerd as an independent service and not managed by docker?

Most likely due to flexibility and since containerd can be used by others too and not just docker.

#### modifying the default behavior of services and daemons

See [drop-in replacement](../systemd.md#modifying-the-behavior-systemd-service-file) for modifying a systemd service file  
So you can create `/etc/systemd/system/containerd.service.d` and `/etc/systemd/system/docker.service.d` directories, and add you custom config files.  
You can overwrite the ExecStart command, service dependencies and other options.

Specific to the command `containerd` , there are 3 ways to modify its behavior:

1. modifying the `/etc/containerd/config.toml` file, which will be merged with the default config. You can see the effective containerd configuration by running `containerd config dump`.

1. passing a custom config file to `containerd` with `--config` flag

1. passing the appropriate flags to the `containerd` itself

#### docker.socket triggers docker.service

If you run `systemctl status docker`, you can see the section "Triggered by" which says `docker.socket`.  
But why?

From the `docker.service` file we can see that it uses [Systemd socket activation](../systemd.md#socket-activation) to create `/run/docker.sock`. Must read [this](../systemd.md#socket-activation-in-case-of-dockerd) article.

Because of systemd socket activation, even if `docker.service` is not running (i.e. dockerd exits), the systemd will take the job of listening to the `docker.sock` file.  Next time running any docker-cli commands (with sudo) will trigger the start of the `dockerd` service.

#### Why not a seperate containerd.socket systemd file?

You can create one, no one's stopping you

But acc to me, docker cli is a client facing tool  
So it has to be ready to work  
We can be sure that containerd will always be spawned due to the dependency chain: Docker.socket - docker.service - containerd.serivce

No one is expected to use nerdctl tool unless they know about containerd and all the stuff we discuss in this article

#### Running dockerd without systemd

##### containerd is not running

If `sudo dockerd` is run, and if `containerd` daemon process is not running in the background, the `dockerd` will spawn a "managed containerd" process with custom config stored in `/var/run/docker/containerd/containerd.toml`.  
This config states that

````ini
disabled_plugins = ["io.containerd.grpc.v1.cri"]
# ...
[grpc]
  address = "/var/run/docker/containerd/containerd.sock"
  state = "/var/run/docker/containerd/daemon"
# ...
````

**Once dockerd is killed, the managed containerd is also killed**  
So in this case dockerd completely owns containerd.

##### containerd is running but containerd.sock is at different location

If containerd is started mannually with `sudo containerd -a /run/containerd-other.sock`  containerd will create the socket at given `/run/containerd-other.sock` location  
To make docker aware of this running containerd instance, we must pass `--containerd /run/containerd-other.sock` option to the `sudo dockerd` command

Else, `dockerd` will first try to search for containerd socket at the default location `/run/containerd/containerd.sock` , and since the socket is not present, it will assume that containerd is not running, and it will start its own managed `containerd`, passing `--config /var/run/docker/containerd/containerd.toml` as flag, which creates socket file at `run/docker/containerd/containerd.sock`

#### some other observations

When --containerd /run/containerd/containerd.sock option is provided to dockerd BUT a containerd daemon is not running in the background, then dockerd will continue to wait till a suitable containerd process runs in the background, which serves the endpoint /run/containerd/containerd.sock . During this wait, any docker-cli command will also wait till dockerd is completely up and running, which is after containerd is up.

When containerd runs in the background, but --containerd option is not provided to sudo dockerd, then also dockerd will not spawn a new containerd, it will detect the already running containerd and use it ("assuming systemd-resolved, so using resolv.conf: /run/systemd/resolve/resolv.conf"). If containerd is killed in between, dockerd will wait till a new containerd process is up, serving the same socket

`nerdctl` command can be made to use either of the running containerd by passing `-a <socket address>` as additional flag  
this is similar to the `context` concept of docker-cli, but there complexities are abstract away. `nerdctl` has no "context" command

## docker in rootless

Need to install docker-rootless-ce-extras package from apt, which is not installed by the standard docker engine installation process

Dockerd runs in user mode (systemd start --user docker)  
Learn more: <https://docs.docker.com/engine/security/rootless/#how-it-works>

For rootless mode, both Docker and podman use rootlesskit  
See more <https://rootlesscontaine.rs/> and <https://github.com/rootless-containers/rootlesskit>

## docker context

Docker context manages the context of the docker and kubernetes  
context includes host (socket) to connect to, ca and tls certs etc.  
See `docker context create --help`

By default, when you install docker (either mac or linux) and if you run docker context ls you will see the "default" context which points to the standard `unix:///var/run/docker.sock` socket

To change context, you need to create another context using docker context create and specify the name and other configs like host, ca, key etc.

Docker contexts is stored in a meta.json file below `~/.docker/contexts/`. Each new context you create gets its own meta.json stored in a dedicated sub-directory of `~/.docker/contexts/` .

You can view the new context with `docker context ls` and `docker context inspect <context-name>`

## cri-docker

<https://github.com/Mirantis/cri-dockerd>

dockerd as a compliant Container Runtime Interface for Kubernetes

A kubernetes kubelet talks to  `cri-dockerd` to start/stop containers. The `cri-dockerd` in turn talks to docker engine `dockerd` , which then talks to `containerd` (and so on...)

Check [this](colima.md#using-cri-dockerd) to see how Minikube can use  `cri-dockerd` to run docker containers.

Note: #toadd add a diagram
