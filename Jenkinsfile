pipeline {
    agent any

    tools {
        jdk 'jdk17'  // Make sure this matches the JDK installed in Jenkins → Manage Jenkins → Global Tool Configuration
    }

    environment {
        SCANNER_HOME = '/opt/sonar-scanner-5.0.1.3006-linux/bin'  // ✅ Update if your scanner path is different
        SONAR_HOST_URL = 'http://192.168.1.4:9000'                 // ✅ Your SonarQube server URL
    }

    stages {
        stage('Clone') {
            steps {
                echo '📥 Cloning repository...'
                checkout scm
            }
        }

        stage('SonarQube Analysis') {
            environment {
                SONAR_AUTH_TOKEN = credentials('SONAR_AUTH_TOKEN_ID')  // ✅ Use Jenkins credentials for your token
            }
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
