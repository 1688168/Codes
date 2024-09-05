> Resources
[Docker Lab](https://labs.play-with-docker.com/)
[Docker getting Started Git: ](https://github.com/nigelpoulton/gsd)


> Containerize an application  
* docker image build -t nigelpoulton/gsd:ctr2023 . //builds an OCI image (docker image)
* docker image ls
* docker image push nigelpoulton/gsd:ctr2023     //push to docker registry (dockerid/nameOfRepo:NameOfImage)
* docker container run -d --name web -p 8080:8080

> List of containers  
* docker container ls -a

> remove container
* docker run --rm # so containers is removed when exit
* docker system prune -a # remove stopped ocntainers, networks, images, build cache

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


```sh
# map/create volumne
* docker run -p <ports> -v $(pwd):/var/www/logs <imageToRun>

# create a bridge network
* docker network create --driver bridge isolated_network_name
* docker network create #create network
* docker network ls #list network
* docker network rm networkName #remove a network
* docker run -d --net=isolated_network --name=mongodb mongo #running a database container in a network

* docker run -d -p 3000:3000 --net=isolated_network --name=nodeapp imageName # running an app container in a network

```

```sh
* docker exec -it <containerId> sh  #shell into a container
```

> key docker compose commands  

```sh
 * docker-compose build
 * docker-compose up
 * docker-compose down
```