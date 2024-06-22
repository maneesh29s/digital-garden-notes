---
aliases: []
author: Maneesh Sutar
date: 2024-05-10
tags:
- public
- linux
- container
title: Colima
---

# Colima

Colima = Containers on [Lima](https://github.com/lima-vm/lima?tab=readme-ov-file) = Containers on Linux on Mac

 > 
 > This article contains my observations from various experiments I conducted with colima. It might be a little unstructured, so bare with me

## Docker with colima

By default, colima uses QEMU VM and Ubuntu 23 as the OS.  
Ubuntu comes with [systemd](../systemd.md). Also, the image used by colima has docker and containerd installed by default, plus their systemd services `docker.service` (along with `docker.socket`) and `containerd.service` are "enabled" to be loaded at boot.  
Thus every default VM in colima **will have docker and containerd running inside**.  
See [docker.service](https://github.com/moby/moby/blob/master/contrib/init/systemd/docker.service) , docker.socket and [containerd.service](https://github.com/containerd/containerd/blob/main/containerd.service) files

To give access to the host Mac, colima uses lima's port forwarding.  
Lima port forwards all the ports for localhost, from 127.0.0.1:1/65535 of VM (guest) to 127.0.0.1:1/65535 of mac (host).  
Additionally, when colima starts with `--runtime=docker` (default), it also forwards the `/var/run/docker.sock` inside VM to `~/.colima/<colima profile/docker.sock` on the host mac.  
Then it runs `docker context create` with appropriate options to create a new context in the host mac's docker (see [the code](https://github.com/abiosoft/colima/blob/8613d5e9d05b2405b6ae6d76df8490c5cd17dadc/environment/container/docker/context.go#L19-L30))  
Thus mac is able to access the docker engine running insde the VM.

When colima starts with `--runtime=containerd`, lima DOES NOT port forward the docker socket (even though docker is running in the VM), thus the host mac can not access the docker engine.

You can see the `lima.yaml` file inside each colima profile in `~/.colima` to see which ports are forwarded.

In colima, once you start a new profile,  
colima port forwards the docker socket inside the VM i.e. `/var/run/docker.sock`  to the host present at `~/.colima/<profile>/docker.sock`  
that's how docker cli on macOS (host) is able to access the dockerd running inside VM.  
See the `~/.colima/_lima/<profile>/lima.yaml` for all port forwarding details

then colima runs docker context create on the host (mac) machine, specifying `--docker host=<path to docker.sock>`. Path to docker.sock depends on the profile.  
For the "colima" (default) profile, it is in `~/.colima/default/docker.sock`  
For the a custom profile say "other", it is in `~/.colima/other/docker.sock`  
Colima will also remove the context once the profile is stopped using colima stop

## Minikube on docker with colima

On mac, minikube can use the docker provided by colima.

The `minikube start` with `--driver=docker` spawns a new container using colima's docker, and that container acts as one of the noes of k8s cluster. If you spawn multiple nodes, each node will be present in a seperate docker container.

As we seen earlier, the default VM in colima **will have docker and containerd running inside**  
spawned by systemd. But the **minikube** runs in an isolated container, and it **does not use the docker or containerd of the colima's VM**.

minicube's docker container runs on Ubuntu 22.04 with systemd. The container is henceforth referred as the k8s node.

minikube supports 3 [CRI](kubernetes.md#CRI): containerd (via cri plugin), cri-o and cri-dockerd

### Using cri-dockerd

The `systemd` inside k8s node spawns `docker.service`, `containerd.service` and `docker.socket`.  
The `dockerd` command listens for the request at the default `/var/run/docker.sock` socket.  
The docker.service uses the modified service file present at `/lib/systemd/system/docker.service` so the `dockerd` command runs with more options than the [default docker.service](https://github.com/moby/moby/blob/master/contrib/init/systemd/docker.service)

Along with above 3 services, the k8s node's systemd also spawns [cri-docker.service](https://github.com/Mirantis/cri-dockerd/blob/master/packaging/systemd/cri-docker.service). and  [cri-docker.socket](https://github.com/Mirantis/cri-dockerd/blob/master/packaging/systemd/cri-docker.socket)  
For the `cri-dockerd` command, the `--container-runtime-endpoint fd://` options specifies `cri-dockerd` to use the `/var/run/cri-docker.sock` spawned using [Socket Activation](../systemd.md#Socket-Activation)

Kubelet is ran with  `--container-runtime-endpoint=unix:///var/run/cri-dockerd.sock` option, thus it sends request to `cri-dockerd` using the `cri-dockerd.sock` socket.

Then, `cri-dockerd` sends request to docker engine (`dockerd`) using the socket present at `/var/run/docker.sock`  (check `cri-dockerd --help` for more default options)

The `docker` cli tool by default talks to the socket present at `/var/run/docker.sock`

Since both `cri-dockerd` and `docker-cli` are talking to the same socket, using `docker ps` command we can see all the running k8s related containers.

 > 
 > The `containerd namespace` in which all k8s containers are running is the docker default "moby"

### Using containerd

When `minikube` is started with `--container-runtime=containerd` ,  
minikube still uses the same VM as k8s node, but all docker related systemd services, `docker.service`, `docker.socket`, `cri-docker.socket`, `cri-docker.service` are disabled.  
Only the `containerd.service` is enabled and running.

Since `dockerd` is not running inside k8s node, so `docker` cli tool will not work.  
We can use `nerdctl` with `--namespace k8s.io` to see the running k8s related containers.  
We can also use `crictl ps` to see the running k8s containers.

The `kubelet` command runs with `--container-runtime-endpoint=unix:///run/containerd/containerd.sock` , thus kubelet sends all the requests directly to the `containerd` using the socket at `run/containerd/containerd.sock`.

Just to test a theory given in this article ["What about docker engine"?](https://kubernetes.io/blog/2018/05/24/kubernetes-containerd-integration-goes-ga/#what-about-docker-engine), inside the k8s node, I ran `dockerd` command by passing the `--containerd=/run/containerd/containerd.sock`. Now both `dockerd` and `kubelet` are talking to the same `containerd` daemon.  So we have a scenario as given in the following image:

![400](Artifacts/containerd_shared_cri_dockerd.png)

A containerd [namespace](https://github.com/containerd/containerd/blob/master/docs/namespaces.md) mechanism is employed to guarantee that Kubelet and Docker Engine won't see or have access to containers and images created by each other. This makes sure they won't interfere with each other. This also means that:

All dockerd spawned things are happening in the default "moby" namespace, accessible by `docker` cli tool  
All kubelet spawned things are happening in the "k8s.io" namespace, accessible by `crictl` tool.

The `nerdctl` (contaiNERD ctl) is a low level cli tool for `containerd`. It can access all the namespaces inside containerd using `-n <name>` option.  
Thus `nerdctl -n moby ps`  will show the running `dockerd` containers, while `nerdctl -n k8s.io ps` will show the running containers spawned by kubelet.

## Colima + k3s

Refer: [k3s vs k8s](https://www.cloudzero.com/blog/k3s-vs-k8s/).

**k3s**: a cli for managing installed k3s cluster. Internally provides other commands like kubectl, crictl etc.

Colima , when creating the vm itself, installs docker engine (irrespective of the runtime) using the official docker engine installation way with apt. So containerd is installed from docker's `containerd.io` package. As seen eariier, docker by default disables "cri" plugin by modifying the `/etc/containerd/config.toml` file

When --kubernetes is passed to colima, it will install "cni" before installing "k3s"  
colima enables cri plugin, by setting `disabled_plugins = []` in `/etc/containerd/config.toml`. Although the actual cri plugin might not start since docker engine does not come with cni.  
cni is installed when colima is run with --kubernetes

### Colima Docker+k3s vs Continerd+k3s

For Docker runtime, images built or pulled with Docker are accessible to Kubernetes.  
For Containerd runtime, images built or pulled in the k8s.io namespace are accessible to Kubernetes.

1. K8s run components in separate processes, whereas K3s combines and operates all control plane components (including kubelet and kube-proxy) in a single binary, server, and Agent process.

1. K3s includes and defaults to *containerd*. Before k8s 1.24, k3s used to have a flag --docker which would enable docker engine in the cluster along with dockershim. Once dockershim support was removed, initially --docker flag was also removed from k3s, forcing users to use container-runtime-endpoint flag to point to cri-dockerd . cri-dockerd was not present in k3s, and had to be installed seperately. The removal of --docker flag from k3s caused systems to fail, so they brought back --docker flag, but now using cri-dockerd . They embedded cri-dockerd along with k3s. More on this on k3s/docs/adrs/cri-dockerd  
   more on this <https://docs.k3s.io/advanced#using-docker-as-the-container-runtime>

1. Colima, based on the --runtime flag, either passes --docker  which starts cri-dockerd and docker engine in k8s cluster, with the default socket path unix:///run/k3s/cri-dockerd/cri-dockerd.sock OR   --container-runtime-endpoint unix:///run/containerd/containerd.sock , so that k3s uses containerd with the custom socket path (default is at unix:///run/k3s/containerd/containerd.sock)

When colima run with `--kubernetes`  
the lima VM itself is the node.  
That's why you see OS = Ubuntu 23.10 which is the OS of the lima VM  
Since the lima VM itself is the node, when you run ps aux | grep k3s you can see that the k3s server is running in the VM itself, and not in any containers.

when `--kubernetes` option is passed to colima start, it will run k3s-install.sh which will install all the k3s components on the VM itself. Based on the --runtime option to colima start, the k3s will either run with containerd or docker + cri-docker

Since the lima VM itself is the node, when you run ps aux | grep k3s you can see that the k3s server is running in the VM itself, and not in any containers.  
Btw, k3s is also spawning some containers when running, namely "k8s_coredns", "k8s_metric-server",k8s_local-path-provisonor" which I don't why. They are related to k3s but they are running in seperate containers instead of running as system process. (either with docker or containerd depending on the runtime). I can not exec into those containers, it throws "OCI runtime exec failed"

`--container-runtime-endpoint` Disables embedded containerd and use the CRI socket at the given path ,  
Colima uses this option since it itself installs containerd runtime on the lima VM, and wishes k3s to use the same runtime

docker does not come embedded with k3s. So when specifying --docker as option, k3s will only start the cri-docker with its default cri endpoint /run/k3s/cri-dockerd/cri-docker.sock , and cri-docker will use the docker daemon being run on the same VM seperately.  
Colima anyway starts the docker daemon on VM with --docker options is specified

## how k8s communication takes place

<https://kubernetes.io/docs/concepts/security/controlling-access/>

for k8s cluster, the port can be changed with the `--secure-port`, and the listening IP address with the `--bind-address` flag.  
this port and ip is stored in the respective context inside the `.kube/config` . This config is read by `kubectl` and it connects to the respective cluster

### k8s by minikube inside a docker container in lima VM (basically colima)

Inside container k8s runs at localhost (127.0.0.1) at some port 8443 (defined by --sercure-port)  
the docker running inside lima VM port forwards 8443 to 32744. this is inside lima VM  
now, lima port forwards all the ports for localhost, from 127.0.0.1:1/65535 of VM (guest) to 127.0.0.1:1/65535 of mac (host)

Thus, the kubectl running on mac (host) is able to access the k8s cluster running at  127.0.0.1:32744

### k3s running in colima VM (i.e. with --kubernetes option)

k3s runs at 127.0.0.1:6443 inside the colima VM  
lima port forwards all the ports for localhost, from 127.0.0.1:1/65535 of VM (guest) to 127.0.0.1:1/65535 of mac (host)

Thus, the kubectl running on mac (host) is able to access the k3s cluster running at  127.0.0.1:6443
