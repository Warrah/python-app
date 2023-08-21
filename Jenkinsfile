pipeline {
    agent any
     tools {
        // Define the Python tool installation by the name you specified in step 2
        python 'MyPython'
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Install Dependencies') {
            steps {
                sh 'python -m venv venv' // Create a virtual environment
                sh 'source venv/bin/activate' // Activate virtual environment
                sh 'pip install uvicorn' // Install project dependencies
            }
        }
        
        
        stage('Build and Deploy') {
            steps {
                sh 'uvicorn your_app:app --host 0.0.0.0 --port 8000 &' // Start Uvicorn server in the background
                sh 'nginx -g "daemon off;"' // Start Nginx to serve your application
            }
        }
    }
    
    post {
        success {
            echo 'Deployment successful!'
        }
        failure {
            echo 'Deployment failed!'
        }
    }
}
