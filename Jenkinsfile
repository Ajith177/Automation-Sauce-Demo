pipeline {
    agent any

    triggers {
        githubPush()
    }

    environment {
        SCANNER_HOME = '/opt/sonar-scanner/bin'
        SONAR_HOST_URL = 'http://192.168.1.4:9000'
        SONAR_AUTH_TOKEN = 'squ_d33310e2786c6e1eb13439d3121f50945aa90fba'
    }

    stages {
        stage('Clone') {
            steps {
                echo 'Cloning repository...'
                checkout scm
            }
        }

        stage('Check Python venv support') {
            steps {
                echo '🔍 Checking python3.10-venv availability...'
                sh '''
                    if ! python3.10 -m venv --help > /dev/null 2>&1; then
                        echo "python3.10-venv is NOT installed!"
                        echo "Run: sudo apt install python3.10-venv"
                        exit 1
                    fi
                    echo "python3.10-venv is installed."
                '''
            }
        }

        stage('Run Unit Tests') {
            steps {
                echo 'Creating venv and running tests...'
                sh '''
                    python3.10 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip setuptools wheel build
                    pip install --only-binary=:all: numpy || true
                    pip install -r requirements.txt
                    python Sauce-demo/test_suite.py > unit_test_report.txt || true
                '''
            }
        }

        stage('SonarQube Analysis') {
            steps {
                echo 'Running SonarQube analysis...'
                withSonarQubeEnv('Mysonarqube') {
                    sh '''
                        ${SCANNER_HOME}/sonar-scanner -X \
                            -Dsonar.projectKey=my_python_automation \
                            -Dsonar.sources=. \
                            -Dsonar.inclusions=**/*.py \
                            -Dsonar.host.url=$SONAR_HOST_URL \
                            -Dsonar.login=$SONAR_AUTH_TOKEN \
                            -Dsonar.python.version=3.10
                    '''
                }
            }
        }

        stage('Quality Gate') {
            steps {
                echo 'Waiting for Quality Gate...'
                script {
                    def qg = waitForQualityGate()
                    if (qg.status != 'OK') {
                        error "Quality Gate failed: ${qg.status}"
                    }
                }
            }
        }

        stage('Trivy Scan') {
            steps {
                echo 'Running Trivy scan...'
                sh 'trivy fs --no-progress --format table -o trivy_report.txt . || true'
            }
        }

        stage('Notify Success') {
            when {
                expression { currentBuild.result == null || currentBuild.result == 'SUCCESS' }
            }
            steps {
                echo 'Sending success email...'
                emailext(
                    subject: "Build Passed: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                    body: """Good news!

The Jenkins pipeline completed successfully

✔ SonarQube Quality Gate passed
✔ Unit tests executed
✔ Trivy scan completed

🔗 Project: ${env.JOB_NAME}
🔗 Build URL: ${env.BUILD_URL}

Reports attached.

""",
                    to: 'loneloverioo@gmail.com',
                    attachmentsPattern: 'unit_test_report.txt,trivy_report.txt'
                )
            }
        }
    }

    post {
        failure {
            echo 'Sending failure email...'
            emailext(
                subject: "Build Failed: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: """The pipeline has failed.

Quality Gate failure
Unit test or build error

Project: ${env.JOB_NAME}
Build URL: ${env.BUILD_URL}
""",
                to: 'loneloverioo@gmail.com'
            )
        }
    }
}
