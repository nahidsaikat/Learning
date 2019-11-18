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
