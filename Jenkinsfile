
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/aditirewadkar3/MLdevopsInternal.git'
            }
        }

        stage('Run Application') {
            steps {
                bat 'python hello.py'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'python -m pytest -v'
            }
        }
    }
}
