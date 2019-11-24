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

## Docker Swarm Command

Free Courses - https://automationstepbystep.com/onli...
Today we will learn :
1. What is Docker Swarm
2. Why to use it
3. How to create and manage Docker Swarm
4. Create service on docker swarm
5. Scaling services up and down
6. Features/Helpful Tips

A swarm is a group of machines that are running Docker and joined into a cluster 
Docker Swarm is a tool for Container Orchestration

Let’s take an example, You have 100 containers, You need to do 
- Health check on every container
- Ensure all containers are up on every system
- Scaling the containers up or down depending on the load
- Adding updates/changes to all the containers

Orchestration - managing and controlling 

multiple docker containers as a single service

Tools available - Docker Swarm, Kubernetes, Apache Mesos

Pre-requisites
1. Docker 1.13 or higher
2. Docker Machine (pre installed for Docker for Windows and Docker for Mac)https://docs.docker.com/machine/insta...
https://docs.docker.com/get-started/p...

Step 1 :  Create Docker machines (to act as nodes for Docker Swarm)   Create one machine as manager and others as workers

    docker-machine create --driver hyperv manager1    docker-machine create --driver virtualbox manager1

   docker-machine:Error with pre-create check: “exit status 126”
   https://stackoverflow.com/questions/3...
   brew cask install virtualbox;

   Create one manager machine
   and other worker machines

Step 2 :  Check machine created successfully

    docker-machine ls
    docker-machine ip manager1

Step 3 :  SSH (connect) to docker machine

    docker-machine ssh manager1

Step 4 :  Initialize Docker Swarm

   docker swarm init --advertise-addr MANAGER_IP

    docker node ls
    (this command will work only in swarm manager and not in worker)

Step 5 :  Join workers in the swarm
    Get command for joining as worker
    In manager node run command

    docker swarm join-token worker
    This will give command to join swarm as worker

    docker swarm join-token manager
    This will give command to join swarm as manager

    SSH into worker node (machine) and run command to join swarm as worker
   
    In Manager Run command - docker node ls to verify worker is registered and is ready
  
    Do this for all worker machines

Step 6 :  On manager run standard docker commands

    docker info
    check the swarm section 
    no of manager, nodes etc

    Now check docker swarm command options 
    docker swarm 

Step 7 :  Run containers on Docker Swarm

    docker service create --replicas 3 -p 80:80 --name serviceName nginx

    Check the status:

    docker service ls
    docker service ps serviceName

    Check the service running on all nodes
    Check on the browser by giving ip for all nodes

Step 8 :  Scale service up and down
   On manager node 

   docker service scale serviceName=2


Inspecting Nodes (this command can run only on manager node)

```docker node inspect nodename

docker node inspect self

docker node inspect worker1
```

Step 9 : Shutdown node

   docker node update --availability drain worker1


Step 10 :  Update service

   docker service update --image imagename:version web
   
   docker service update --image nginx:1.14.0 serviceName

Step 11 :  Remove service

   docker service rm serviceName

docker swarm leave : to leave the swarm

docker-machine stop machineName : to stop the machine

docker-machine rm machineName : to remove the machine


REFERENCES:
https://docs.docker.com/get-started/p...
https://rominirani.com/docker-swarm-t...


FAQs & Helpful Tips:

A swarm is a group of machines that are running Docker and joined into a cluster

A cluster is managed by swarm manager
The machines in a swarm can be physical or virtual. After joining a swarm, they are referred to as nodes

Swarm managers are the only machines in a swarm that can execute your commands, or authorise other machines to join the swarm as workers

Workers are just there to provide capacity and do not have the authority to tell any other machine what it can and cannot do

you can have a node join as a worker or as a manager. At any point in time, there is only one LEADER and the other manager nodes will be as backup in case the current LEADER opts out

https://www.youtube.com/watch?v=bU2NNFJ-UXA&list=PLhW3qG5bs-L99pQsZ74f-LC-tOEsBp2rK&index=16&t=0s
