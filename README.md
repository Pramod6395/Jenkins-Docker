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
   && apt-get install -y docker-ce

RUN usermod -aG docker jenkins

RUN apt-get update -qq \
   && apt-get install -y sshpass


```
2. Build the image from above file.
```
docker image build -t jenkins-docker .
```
3. Run the container once image is Build.
```
docker container run -d -p 8080:8080 -v /var/run/docker.sock:/var/run/docker.sock jenkins-docker 
```
  You can also enter in jenkins conatner haveing file at **/var/jenkins_home**.
```
docker exec -it [containerID] bash
```
4. Your Jenkins with using host docker daemon is ready and you can access it with below ip.
```
http://localhost:8080
```
5. Get password using below command.
```
docker exec [containerID] cat /var/jenkins_home/secrets/initialAdminPassword
```
Put this password and install suggested plugins [ it may take 2-3 try]

#### Steps for building docker image and push to dockerhub.

Before doing anything makesure **Docker** and **Docker Pipeline** Plugings are installed in Jenkings.

   ![image](https://github.com/Pramod6395/Jenkins-Docker/assets/73251890/0a61b4e6-1708-4ad1-ade6-74e02438c402)


1. Go on Jenking Dashboard>>New>> and give the name to pipeline "docker_image_pipeline" and select "pipeline" then click ok.

    ![image](https://github.com/Pramod6395/Jenkins-Docker/assets/73251890/f23f2f28-2d1d-43f4-82a1-e0e6080f58a2)

2. This will open the pipeline configration page so just scroll down on Pipeline defination section and select from dropdown "Pipeline script from SCM"
   also select SCM as "GIT" and put repository URL "https://github.com/Pramod6395/Jenkins-Docker" (in your case its your") and put branch as "main" and save.
    ![image](https://github.com/Pramod6395/Jenkins-Docker/assets/73251890/89e041fd-d8c9-4058-9426-f4f860a22f7e)

3. Save the DockerHub credential go to Dashboard>>Manage Jenkins>>Manage credential>>global>>Add Credential>> put username and token/ password for dockerhub and Save.
   We can use "ID" which is "dockerhub_id" in our Jenkinsfile to refere to the dockerhub credential.

   ![image](https://github.com/Pramod6395/Jenkins-Docker/assets/73251890/022dfe44-f726-48a8-9ef2-bd7a91cde9a3)
   
4. Save SSH credential to do ssh to another server to deploy the application.
    ![image](https://github.com/Pramod6395/Jenkins-Docker/assets/73251890/0895f98d-84f7-43f3-a955-e54238abd01b)


5. Create all the file which are given in this repo in Your Repo before performing Build.
   Make sure to do changes in JenkingFile according to your **github url** and **dockerHub username** and production server IP.
   
  ```
  pipeline {
    agent any

    stages {
        stage('Clone Git Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/Pramod6395/Jenkins-Docker.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("pramopatil95/python-flask-app:${env.BUILD_NUMBER}")
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', 'dockerhub_id') {
                        docker.image("pramopatil95/python-flask-app:${env.BUILD_NUMBER}").push()
                    }
                }
            }
        }

        stage('SSH to Remote Server') {
            steps {
                script {
                    withCredentials([
                        usernamePassword(credentialsId: 'ami_pc', passwordVariable: 'SSH_PASSWORD', usernameVariable: 'SSH_USERNAME')
                    ]) {
                        sh """
                            sshpass -p '${SSH_PASSWORD}' ssh ${SSH_USERNAME}@199.199.50.138 'mkdir -p /home/ami/DockerTest'
                            sshpass -p '${SSH_PASSWORD}' ssh ${SSH_USERNAME}@199.199.50.138 'docker stop my-container || true'
                            sshpass -p '${SSH_PASSWORD}' ssh ${SSH_USERNAME}@199.199.50.138 'docker rm my-container || true'
                            sshpass -p '${SSH_PASSWORD}' ssh ${SSH_USERNAME}@199.199.50.138 'docker pull pramopatil95/python-flask-app:${env.BUILD_NUMBER}'
                            sshpass -p '${SSH_PASSWORD}' ssh ${SSH_USERNAME}@199.199.50.138 'docker run -d -p 5000:5000 --name my-container pramopatil95/python-flask-app:${env.BUILD_NUMBER}'
                        """
                    }
                }
            }
        }
    }
}
```
7. Go to Dashboard>>Pipeline docker_image_pipeline>>Build Now.

   ![image](https://github.com/Pramod6395/Jenkins-Docker/assets/73251890/3be26d54-d600-42c2-ad7a-925034035dbb)
   
7. You can Check logs of steps in colsole output after clicking on Build Run number.
   ![image](https://github.com/Pramod6395/Jenkins-Docker/assets/73251890/ede7ab73-6e3f-4f1e-9203-95d6bc590401)

8. This will clone the git repo Build the image and push to DockerHub then ssh to another server and deploy container on it you can check on DockerHub.
  ![image](https://github.com/Pramod6395/Jenkins-Docker/assets/73251890/8881d6c8-5a5e-4988-937d-df0f157f4db0)
