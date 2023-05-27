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
