# Docker 

## Docker Images Command

* docker images --help
* docker pull image
* docker images
* docker images -q
* docker images -f “dangling=false”
* docker images -f “dangling=false” -q

* docker run image
* docker rmi image
* docker rmi -f image

* docker inspect
* docker history imageName

https://www.youtube.com/watch?v=QBOcKdh-fwQ&list=PLhW3qG5bs-L99pQsZ74f-LC-tOEsBp2rK&index=10&t=0s

## Docker Containers Command

* docker ps
* docker run ImageName
* docker start ContainerName/ID
* docker stop ContainerName/ID

* docker pause ContainerName/ID
* docker unpause  ContainerName/ID

* docker top ContainerName/ID
* docker stats ContainerName/ID

* docker attach ContainerName/ID

* docker kill ContainerName/ID
* docker rm ContainerName/ID

* docker history ImageName/ID

https://www.youtube.com/watch?v=Rv3DAJbDrS0&list=PLhW3qG5bs-L99pQsZ74f-LC-tOEsBp2rK&index=11&t=0s

## Docker File Command

* docker build 
* docker build -t ImageName:Tag directoryOfDocekrfile

* docker run image

https://www.youtube.com/watch?v=LQjaJINkQXY&list=PLhW3qG5bs-L99pQsZ74f-LC-tOEsBp2rK&index=13&t=0s

https://github.com/wsargent/docker-cheat-sheet#dockerfile
https://docs.docker.com/engine/reference/builder/#environment-replacement

## Docker Compose Command

Step 1 : install docker compose
   (already installed on windows and mac with docker)
   docker-compose -v
   
   2 Ways

   1.  https://github.com/docker/compose/rel...

   2. Using PIP
    pip install -U docker-compose

Step 2 : Create docker compose file at any location on your system
   docker-compose.yml

Step 3 : Check the validity of file by command
    docker-compose config

Step 4 : Run docker-compose.yml file by command
   docker-compose up -d

Steps 5 : Bring down application by command
   docker-compose down

TIPS
How to scale services

—scale
docker-compose up -d --scale database=4

https://www.youtube.com/watch?v=HUpIoF_conA&list=PLhW3qG5bs-L99pQsZ74f-LC-tOEsBp2rK&index=14&t=0s

## Docker Volume Command

* docker volume  //get information
* docker volume create
* docker volume ls
* docker volume inspect
* docker volume rm
* docker volume prune

Use of Volumes
* Decoupling container from storage
* Share volume (storage/data) among different containers
* Attach volume to container
* On deleting container volume does not delete

Commands
* docker run --name MyJenkins1 -v myvol1:/var/jenkins_home -p 8080:8080 -p 50000:50000 jenkins
* docker run --name MyJenkins2 -v myvol1:/var/jenkins_home -p 9090:8080 -p 60000:50000 jenkins
* ocker run --name MyJenkins3 -v /Users/raghav/Desktop/Jenkins_Home:/var/jenkins_home -p 9191:8080 -p 40000:50000 jenkins

References
https://hub.docker.com/_/jenkins/
https://docs.docker.com/storage/volumes/

NOTES

* By default all files created inside a container are stored on a writable container layer

* The data doesn’t persist when that container is no longer running

* A container’s writable layer is tightly coupled to the host machine where the container is running. You can’t easily move the data somewhere else.

* Docker has two options for containers to store files in the host machine
so that the files are persisted even after the container stops

VOLUMES  and  BIND MOUNTS

* Volumes are stored in a part of the host filesystem which is managed by Docker

* Non-Docker processes should not modify this part of the filesystem

* Bind mounts may be stored anywhere on the host system

* Non-Docker processes on the Docker host or a Docker container can modify them at any time

* In Bind Mounts, the file or directory is referenced by its full path on the host machine. 


* Volumes are the best way to persist data in Docker

* volumes are managed by Docker and are isolated from the core functionality of the host machine

* A given volume can be mounted into multiple containers simultaneously.

* When no running container is using a volume, the volume is still available to Docker and is not removed automatically. You can remove unused volumes using docker volume prune.

* When you mount a volume, it may be named or anonymous. 

* Anonymous volumes are not given an explicit name when they are first mounted into a container

* Volumes also support the use of volume drivers, which allow you to store your data on remote hosts or cloud providers, among other possibilities.

https://www.youtube.com/watch?v=VOK06Q4QqvE&list=PLhW3qG5bs-L99pQsZ74f-LC-tOEsBp2rK&index=15&t=0s

