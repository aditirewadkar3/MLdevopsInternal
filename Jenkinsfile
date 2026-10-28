
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Using the repository already checked out by Jenkins'
                bat 'git remote -v'
            }
        }

        stage('Run Application') {
            steps {
                bat 'python --version'
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
