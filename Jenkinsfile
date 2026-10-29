
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
                bat '"C:\Users\Mohin\AppData\Local\Microsoft\WindowsApps\python.exe" --version'
                bat '"C:\Users\Mohin\AppData\Local\Microsoft\WindowsApps\python.exe" hello.py'
            }
        }

        stage('Run Tests') {
            steps {
                bat '"C:\Users\Mohin\AppData\Local\Microsoft\WindowsApps\python.exe" -m pytest -v'
            }
        }
    }
}
