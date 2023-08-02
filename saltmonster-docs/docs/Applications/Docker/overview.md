# Containers


### Namespaces

Namepaces provide an isolated workplace from the host server.  Docker containers have several (pid, net, ipc, mnt, utls, user) 

### Control Groups

Groups conainers processes for resource management (cpu time, system memory, network bandwidth)

### Commands

Command | Description
--------| -----------
docker run hello-world | Download, build 
docker build --file server.Dockerfile --tag test-server . | Build a container
docker run -d docker run -d --name test-server -p 5001:5000 test-server | Assign a local port to a container portout-first-server | Run a detached container
docker run -d -p 80:80 -v "$(pwd)/website":/usr/share/nginx/html nginx | Run a container with local ports and attach a local volume
docker exec test-container date | Execute date on the container
docker exec -it test-container bash | Attach an interactive session to a container
docker logs test-container | Show the logs from a container
docker logs -f test-container | Show the stdout of a container
docker ps | Show running containers
docker ps -a | Show all containers regardless if they are running
docker ps -aq | Show only the conainer id's useful to pass onto another script (xargs)
docker stop test-container | Stop a container
docker rm 639977ddfa5e | Remove a container
docker rm -f test-container | Remove a container by force
docker pull ubuntu:xenial | Pull an image local from docker hub
docker image ls | List all local images
docker images | List all local images
docker rmi nginx | Remove a local image
docker inspect nginx | Show all image information
