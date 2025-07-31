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
                echo 'Cloning repository...'
                checkout scm
            }
        }

        stage('Check Python 3.11 venv support') {
            steps {
                echo 'Checking python3.11-venv availability...'
                sh '''
                    if ! python3.11 -m venv --help > /dev/null 2>&1; then
                        echo "python3.11-venv is NOT installed!"
                        echo "Run: sudo apt install python3.11-venv python3.11-dev"
                        exit 1
                    fi
                    echo "python3.11-venv is installed."
                '''
            }
        }

        stage('Run Unit Tests') {
            steps {
                echo 'Creating Python 3.11 virtual environment and running unit tests...'
                sh '''
                    rm -rf venv
                    python3.11 -m venv venv
                    . venv/bin/activate
                    python -m pip install --upgrade pip setuptools wheel
                    pip install --only-binary=:all: numpy || true
                    pip install -r requirements.txt
                    python Sauce-demo/test_suite.py > unit_test_report.txt || true
                '''
            }
        }

        stage('SonarQube Analysis') {
            steps {
                echo '🔎 Running SonarQube analysis...'
                withSonarQubeEnv('Mysonarqube') {
                    sh '''
                        ${SCANNER_HOME}/sonar-scanner -X \
                            -Dsonar.projectKey=my_python_automation \
                            -Dsonar.sources=. \
                            -Dsonar.inclusions=**/*.py \
                            -Dsonar.host.url=$SONAR_HOST_URL \
                            -Dsonar.login=$SONAR_AUTH_TOKEN \
                            -Dsonar.python.version=3.11
                    '''
                }
            }
        }

        stage('Quality Gate') {
            steps {
                echo 'Waiting for SonarQube Quality Gate...'
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
                echo 'Running Trivy vulnerability scan...'
                sh '''
                    trivy fs --no-progress --format table -o trivy_report.txt . || true
                '''
            }
        }

        stage('Notify Success') {
            when {
                expression { currentBuild.result == null || currentBuild.result == 'SUCCESS' }
            }
            steps {
                echo '📧 Sending success email...'
                emailext(
                    subject: "✅ Build Passed: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                    body: """Good news!

The Jenkins pipeline completed successfully.

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
            echo '📧 Sending failure email...'
            emailext(
                subject: "Build Failed: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: """The pipeline has failed.

⚠️ Reason could be:
- Quality Gate failed
- Unit test or environment setup issue

🔗 Project: ${env.JOB_NAME}
🔗 Build URL: ${env.BUILD_URL}
""",
                to: 'loneloverioo@gmail.com'
            )
        }
    }
}
