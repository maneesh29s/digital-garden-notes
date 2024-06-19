---
aliases: []
author: Maneesh Sutar
date: 2024-05-06
tags:
- public
- linux
title: systemd
---

# systemd

systemd blog: <https://0pointer.de/blog/projects/systemd.html>

Its the "init" process in linux which runs with PID 1.  
Its the parent of all processes.

Linux traditionally has "System V init" as the init process.

But systemd gives performance improvment by using variaous techniques. Also systemd has more features than System V init.

To get the logs (stdout) of a systemctl service:  
`sudo journalctl -u <service name> | less`

## Socket Activation

One of the main advantage of systemd is "Socket Activation"

socket activation blog: <https://0pointer.de/blog/projects/socket-activation.html>

Also see [systemd.socket(5)](https://manpages.debian.org/testing/systemd/systemd.socket.5.en.html)

Systemd loads all the required sockets at the boot itself, and starts listening to them on behalf of the real service (which has not yet started).  
Once a client performs a request to the socket, 2 things happen parallely

1. systemd listens and keeps track of all the requests in a message queye

1. systemd starts the corresponding service (the application)  
   once the service is loaded completely, systemd transfers the ownership of the socket to that service. The service will then listen to the socket and perform whatever action is wants to.

Because of socket activation,

1. We no longer need to configure dependencies explicitly. Since the sockets are initialized before all services they are simply available.

1. Typically service owns the socket, so it starts the socket and also kills it before terminating. With systemd socket activation, The listening socket stays around, not losing a single message. So even if the service crashes and restarts / OR service is upgraded / service is replaced with another, we make sure that service is continously responsive since socket is always present. Not a single connection is lost during the transition.

### Socket activation in case of Dockerd

Background: dockerd (docker daemon) is a background process (the server), and the docker-cli (docker command in terminal) is the client.  
docker-cli talks to dockerd using UNIX, tcp or fd sockets.  
By default, a `unix` domain socket (or IPC socket) is created at `/var/run/docker.sock`

Without systemd: dockerd can be started mannually using `sudo dockerd`  command. It will create the socket at the default `/run/docker.sock`  
Once dockerd is killed, the socket is also lost.

With systemd:  
Have a look at the `docker.service` and `docker.socket` files in [docker source tree](https://github.com/moby/moby/tree/master/contrib/init/systemd)  
docker.service "wants" docker.socket  
systemd will make sure to start docker.socket first, and then docker.service on demand (at the first request to socket)

 > 
 > By default, systemd matches the filename before ".service" and ".socket" suffixes to decide which socket should trigger which service. This can be modified in the socket file using `=Service` option

Also the dockerd command in docker.service contains  `-H fd://` option. This option forces dockerd to use systemd socket activation to get the socket from systemd INSTEAD of dockerd creating a new socket on its own.  
<https://stackoverflow.com/questions/43303507/what-does-fd-mean-exactly-in-dockerd-h-fd>

systemd loads starts these sockets and services at boot (if "enabled" to start at boot) OR you can start these services mannually using `systemctl start`

## modifying the behavior systemd service file

Say is the service running is present in file "/lib/systemd/system/docker.service"  
then create a folder called "/etc/systemd/system/docker.service.d" (with '.d' at the end of the service name\_  
Inside this folder, all the conf files you create will be used by systemd daemon as drop-in replace for the "docker" service

<https://stackoverflow.com/questions/59842743/what-is-a-drop-in-file-what-is-a-drop-in-directory-how-to-edit-systemd-service>
