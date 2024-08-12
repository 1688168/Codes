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