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
#### Steps for building docker image and push to dockerhub.

1. Go on Jenking Dashboard>>New>> and give the name to pipeline "docker_image_pipeline" and select "pipeline" then click ok.

![image](https://github.com/Pramod6395/Jenkins-Docker/assets/73251890/f23f2f28-2d1d-43f4-82a1-e0e6080f58a2)

2. This will open the pipeline configration page so just scroll down on Pipeline defination section and select from dropdown "Pipeline script from SCM"
   also select SCM as "GIT" and put repository URL "https://github.com/Pramod6395/Jenkins-Docker" (in your case its your") and put branch as "main" and save.
   ![image](https://github.com/Pramod6395/Jenkins-Docker/assets/73251890/89e041fd-d8c9-4058-9426-f4f860a22f7e)

3. Save the DockerHub credential go to Dashboard>>Manage Jenkins>>Manage credential>>global>>Add Credential>> put username and token/ password for dockerhub and Save.
   We can use "ID" which is "dockerhub_id" in our Jenkinsfile to refere to the dockerhub credential.

![image](https://github.com/Pramod6395/Jenkins-Docker/assets/73251890/022dfe44-f726-48a8-9ef2-bd7a91cde9a3)


