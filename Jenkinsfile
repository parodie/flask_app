pipeline{
    agent any

    environment {
        IMAGE_NAME = "my-flask-app"
        CONTAINER_NAME = "flask-app-container"
    }

    stages{
        stage('Test Docker') {
            steps {
                sh 'docker --version'
                sh 'docker info'
            }
        }
        stage('Cloning Repository'){
            steps{
                echo 'Cloning the Git repo...'
                git branch: 'main',
                    url: 'https://github.com/parodie/flask_app.git'
            }
        }
        stage('Building Docker image'){
            steps{
                echo 'Building the Docker image...'
                sh 'docker build -t ${IMAGE_NAME}:latest .'
            }
        }
        stage('Deploy as Container') {
            steps {
                echo 'Deploying Flask app...'
                sh '''
                    docker stop ${CONTAINER_NAME} || true
                    docker rm ${CONTAINER_NAME} || true
                    docker run -d --name ${CONTAINER_NAME} -p 5000:5000 ${IMAGE_NAME}:latest
                '''
            }
        }
        stage('Running Tests'){
            steps{
                echo 'Running tests on the Flask app...'
                sh '''
                    docker run --rm ${IMAGE_NAME}:latest python -m pytest test_app.py -v
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline succeeded! App is running at http://localhost:5000'
        }
        failure {
            echo 'Pipeline failed!'
        }
        always {
            cleanWs()  // Optional: clean workspace
        }
    }
}