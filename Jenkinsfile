pipeline {
    agent {
        label 'docker-agent-python'
       }

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
    }
}

