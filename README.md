# Jenkins-Docker

#### Installation of Jenkings in Docker.
 1. Copy the below Dockerfile
 ```
FROM jenkins/jenkins:lts

USER root

RUN apt-get update -qq \
    && apt-get install -qqy apt-transport-https ca-certificates curl gnupg2 software-properties-common 

RUN curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add -

RUN add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/debian \
   $(lsb_release -cs) \
   stable"

RUN apt-get update  -qq \
    && apt-get install docker-ce -y

RUN usermod -aG docker jenkins

```
2. Build the image from above file.
```
docker image build -t jenkins-docker .
```
3. Run the container once image is Build.
```
docker container run -d -p 8080:8080 -v /var/run/docker.sock:/var/run/docker.sock jenkins-docker 
```
4. Your Jenkins with using host docker daemon is ready and you can access it with below ip.
```
http://localhost:8080
```
