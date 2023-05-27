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
            environment {
                SSH_PASSWORD = credentials('ssh-password').password
            }
            steps {
                script {
                    sh '''
                        sshpass -p "${SSH_PASSWORD}" ssh ${SSH_USERNAME}@199.199.50.138 'mkdir -p /home/ami/DockerTest'
                        sshpass -p "${SSH_PASSWORD}" ssh ${SSH_USERNAME}@199.199.50.138 'docker stop my-container || true'
                        sshpass -p "${SSH_PASSWORD}" ssh ${SSH_USERNAME}@199.199.50.138 'docker rm my-container || true'
                        sshpass -p "${SSH_PASSWORD}" ssh ${SSH_USERNAME}@199.199.50.138 'docker pull pramopatil95/python-flask-app:${env.BUILD_NUMBER}'
                        sshpass -p "${SSH_PASSWORD}" ssh ${SSH_USERNAME}@199.199.50.138 'docker run -d -p 8080:80 --name my-container -v /home/ami/DockerTest:/app pramopatil95/python-flask-app:${env.BUILD_NUMBER}'
                    '''
                }
            }
        }
    }
}
