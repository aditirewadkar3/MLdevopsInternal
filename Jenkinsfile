
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Repository checked out successfully'
                bat 'git remote -v'
            }
        }

        stage('Check Python') {
            steps {
                bat '"C:\\Program Files\\Python311\\python.exe" --version'
            }
        }

        stage('Run Application') {
            steps {
                bat '"C:\\Program Files\\Python311\\python.exe" hello.py'
            }
        }

        stage('Run Tests') {
            steps {
                bat '"C:\\Program Files\\Python311\\python.exe" -m pytest -v'
            }
        }
    }
}
