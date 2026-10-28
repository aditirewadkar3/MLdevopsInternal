
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Repository checked out successfully'
                bat 'git remote -v'
            }
        }

        stage('Run Application') {
            steps {
                bat '"C:/Users/Aditi/AppData/Local/Programs/Python/Python311/python.exe" --version'
                bat '"C:/Users/Aditi/AppData/Local/Programs/Python/Python311/python.exe" hello.py'
            }
        }

        stage('Run Tests') {
            steps {
                bat '"C:/Users/Aditi/AppData/Local/Programs/Python/Python311/python.exe" -m pytest -v'
            }
        }
    }
}
