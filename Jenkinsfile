pipeline {
    agent any

    triggers {
        githubPush()
    }

    environment {
        SCANNER_HOME = '/opt/sonar-scanner-5.0.1.3006-linux/bin'
        SONAR_HOST_URL = 'http://192.168.1.4:9000'
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
                withSonarQubeEnv('Mysonarqube') {
                    sh """
                        ${SCANNER_HOME}/sonar-scanner -X \
                            -Dsonar.projectKey=my_python_automation \
                            -Dsonar.sources=. \
                            -Dsonar.inclusions=**/*.py \
                            -Dsonar.host.url=${SONAR_HOST_URL} \
                            -Dsonar.login=${SONAR_AUTH_TOKEN} \
                            -Dsonar.python.version=3.10
                    """
                }
            }
        }

        stage('Quality Gate') {
            steps {
                echo '⏳ Waiting for quality gate result...'
                script {
                    def qg = waitForQualityGate()
                    if (qg.status != 'OK') {
                        error "❌ Quality Gate failed: ${qg.status}"
                    }
                }
            }
        }

        stage('Trivy Scan') {
            steps {
                echo '🔍 Running Trivy scan on project files...'
                script {
                    sh 'trivy fs --no-progress --format table -o trivy_report.txt .'
                }
            }
        }


        stage('Notify Success') {
            when {
                expression { currentBuild.result == null || currentBuild.result == 'SUCCESS' }
            }
            steps {
                emailext(
                    subject: "✅ Build Passed: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                    body: """Good news! 🎉

The build completed successfully and passed the SonarQube Quality Gate.

🔍 Trivy scan report is attached for your review.

📦 Project: ${env.JOB_NAME}
🔗 Build URL: ${env.BUILD_URL}
""",
                    to: 'loneloverioo@gmail.com',
                    attachmentsPattern: 'trivy_report.txt'
                )
            }
        }
    }

    post {
        failure {
            emailext(
                subject: "❌ Build Failed: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: """Unfortunately, the pipeline has failed. 😞

This could be due to:
- SonarQube Quality Gate failure
- Jenkins stage failure

📦 Project: ${env.JOB_NAME}
🔗 Build URL: ${env.BUILD_URL}
""",
                to: 'loneloverioo@gmail.com'
            )
        }
    }
}
