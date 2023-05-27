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
                        usernamePassword(credentialsId: 'us_server_id', passwordVariable: 'SSH_PASSWORD', usernameVariable: 'SSH_USERNAME')
                    ]) {
                        sh """
                            sshpass -p '${SSH_PASSWORD}' ssh ${SSH_USERNAME}@71.184.122.66 'mkdir -p /home/cimcon/DockerTest'
                            sshpass -p '${SSH_PASSWORD}' ssh ${SSH_USERNAME}@71.184.122.66 'docker stop my-container || true'
                            sshpass -p '${SSH_PASSWORD}' ssh ${SSH_USERNAME}@71.184.122.66 'docker rm my-container || true'
                            sshpass -p '${SSH_PASSWORD}' ssh ${SSH_USERNAME}@71.184.122.66 'docker pull pramopatil95/python-flask-app:${env.BUILD_NUMBER}'
                            sshpass -p '${SSH_PASSWORD}' ssh ${SSH_USERNAME}@71.184.122.66 'docker run -d -p 5000:5000 --name my-container pramopatil95/python-flask-app:${env.BUILD_NUMBER}'
                        """
                    }
                }
            }
        }
    }
}
