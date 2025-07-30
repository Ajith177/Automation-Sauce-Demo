pipeline {
    agent any

    tools {
    jdk 'JDK17'
   }

     triggers {
        githubPush()
    }

    environment {
        SCANNER_HOME = '/opt/sonar-scanner-5.0.1.3006-linux/bin'
        SONAR_HOST_URL = 'http://192.168.1.4:9000'                 // ✅ Your SonarQube server URL
        SONAR_AUTH_TOKEN = 'squ_d33310e2786c6e1eb13439d3121f50945aa90fba'
    }

    stages {
        stage('Clone') {
            steps {
                echo '📥 Cloning repository...'
                checkout scm
            }
        }

        stage('SonarQube Analysis') {
            steps {
                echo '🔍 Starting SonarQube analysis...'
                withSonarQubeEnv('Mysonarqube') {  // ✅ This name must match Jenkins > Manage Jenkins > Configure System > SonarQube Servers
                    sh """
                        ${SCANNER_HOME}/sonar-scanner \
                        -Dsonar.projectKey=my_python_automation \
                        -Dsonar.sources=. \
                        -Dsonar.host.url=${SONAR_HOST_URL} \
                        -Dsonar.login=${SONAR_AUTH_TOKEN} \
                        -Dsonar.python.version=3.10
                    """
                }
            }
        }

        stage('Success') {
            steps {
                echo '✅ Jenkins pipeline completed successfully.'
            }
        }
    }
}
