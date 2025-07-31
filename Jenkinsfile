pipeline {
    agent any

    triggers {
        githubPush()
    }

    environment {
        SCANNER_HOME = '/opt/sonar-scanner-5.0.1.3006-linux/bin'
        SONAR_HOST_URL = 'http://192.168.1.4:9000'
        SONAR_AUTH_TOKEN = 'squ_d33310e2786c6e1eb13439d3121f50945aa90fba'
        ALLURE_DEPLOY_DIR = '/var/www/html/allure'
    }

    stages {

        stage('Clone') {
            steps {
                echo '🔄 Cloning repository...'
                checkout scm
            }
        }

        stage('Check Python 3.11 venv') {
            steps {
                echo '🔍 Checking python3.11-venv...'
                sh '''
                    if ! python3.11 -m venv --help > /dev/null 2>&1; then
                        echo "python3.11-venv is NOT installed!"
                        echo "Run: sudo apt install python3.11-venv python3.11-dev"
                        exit 1
                    fi
                '''
            }
        }

        stage('Run Unit Tests + Allure') {
            steps {
                echo '🧪 Running unit tests with Allure reporting...'
                sh '''
                    rm -rf venv allure-results
                    python3.11 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip setuptools wheel
                    pip install -r requirements.txt
                    pip install allure-pytest
                    pytest Sauce-demo/test_suite.py --alluredir=allure-results > unit_test_report.txt || true
                '''
            }
        }

        stage('Allure Report') {
            steps {
                echo '📊 Generating Allure Report and deploying to Nginx...'
                sh '''
                    rm -rf allure-report
                    /opt/allure/bin/allure generate allure-results -o allure-report
                    mkdir -p /var/lib/jenkins/allure-public
                    rm -rf /var/lib/jenkins/allure-public/*
                     cp -r allure-report/* /var/lib/jenkins/allure-public/
                '''
            }
        }

        stage('SonarQube Analysis') {
            steps {
                echo '🔎 SonarQube scanning.......'
                withSonarQubeEnv('Mysonarqube') {
                    sh '''
                        ${SCANNER_HOME}/sonar-scanner -X \
                          -Dsonar.projectKey=my_python_automation \
                          -Dsonar.sources=. \
                          -Dsonar.exclusions=venv/**,**/site-packages/**,**/__pycache__/** \
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
                echo '✅ Waiting for SonarQube Quality Gate...'
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
                echo '🔐 Running Trivy vulnerability scan...'
                sh '''
                    trivy fs --no-progress --format table -o trivy_report.txt . || true
                '''
            }
        }

        stage('Allure Report in Jenkins UI') {
            steps {
                echo '📊 Publishing Allure Report to Jenkins UI...'
                allure includeProperties: false,
                       jdk: '',
                       reportBuildPolicy: 'ALWAYS',
                       results: [[path: 'allure-results']]
            }
        }

        stage('Notify Success') {
            when {
                expression { currentBuild.result == null || currentBuild.result == 'SUCCESS' }
            }
            steps {
                echo '📧 Sending success email...'
                sh 'zip -r allure-report.zip allure-results || true'
                emailext(
                    subject: "✅ Build Passed: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                    body: """Good news!

✔ SonarQube Quality Gate passed
✔ Unit tests executed
✔ Trivy scan completed
✔ Allure report published

🔗 Jenkins Job: ${env.JOB_NAME}
🔗 Build URL: ${env.BUILD_URL}
🔗 Allure Report: http://192.168.1.4:8081
""",
                    to: 'loneloverioo@gmail.com',
                    attachmentsPattern: 'unit_test_report.txt,trivy_report.txt,allure-report.zip'
                )
            }
        }
    }

    post {
        failure {
            echo '📧 Sending failure email...'
            emailext(
                subject: "❌ Build Failed: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: """The pipeline has failed.

⚠️ Possible issues:
- Quality Gate failure
- Unit test errors
- Trivy scan findings

🔗 Jenkins Job: ${env.JOB_NAME}
🔗 Build URL: ${env.BUILD_URL}
""",
                to: 'loneloverioo@gmail.com'
            )
        }
    }
}
