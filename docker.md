> Resources
[Docker Lab](https://labs.play-with-docker.com/)
[Docker getting Started Git: ](https://github.com/nigelpoulton/gsd)


> Containerize an application  
* docker image build -t nigelpoulton/gsd:ctr2023 . //builds an OCI image (docker image)
* docker image ls
* docker image push nigelpoulton/gsd:ctr2023     //push to docker registry (dockerid/nameOfRepo:NameOfImage)
* docker container run -d --name web -p 8080:8080



> Terminologies:  
* OCI: Open Container Initiative

> Network:
* docker network create
* docker network ls
* docker network rm [network]

> Shell into a container:  
* docker exec -it <containerId> sh

> Building a Custom Image  

```sh
* docker build -t <name> .
# -t: short for --tag
# .: build context from current directory

* docker build -t <registry>/<name>:<tag> .

# List docker images
* docker images

# remove an image
* docker rmi <imageId>

# deploy an image to Docker Hub
* docker push <user name>/<image name>:<tag>

# running a container
* docker run -p <externalPort>:<internalPort>

```