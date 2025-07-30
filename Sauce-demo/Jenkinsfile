pipeline {
    agent any

    environment {
        SONARQUBE_SERVER = 'Mysonarqube' // Must match name in Jenkins > Global Tool Configuration
        SONAR_PROJECT_KEY = 'my_python_automation'
        SONAR_HOST_URL = 'http://192.168.1.4:9000'
        SONARQUBE_TOKEN = credentials('sonar_token_id') // Jenkins > Credentials > Secret Text
    }

    stages {
        stage('Clone') {
            steps {
                echo "Cloning the repository..."
                checkout scm
            }
        }

        stage('SonarQube Scan') {
            steps {
                echo "Running SonarQube analysis..."
                withSonarQubeEnv("${SONARQUBE_SERVER}") {
                    sh """
                        sonar-scanner \
                        -Dsonar.projectKey=$SONAR_PROJECT_KEY \
                        -Dsonar.sources=. \
                        -Dsonar.host.url=$SONAR_HOST_URL \
                        -Dsonar.login=$SONARQUBE_TOKEN
                    """
                }
            }
        }


        stage('Build') {
            steps {
                echo "Build stage (optional)..."
                // Add your build steps here
            }
        }

        stage('Test') {
            steps {
                echo "Test stage (optional)..."
                // Add your test steps here
            }
        }

        stage('Deploy') {
            steps {
                echo "Deploy stage (optional)..."
                // Add your deployment steps here
            }
        }
    }
}
