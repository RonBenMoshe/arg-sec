pipeline{
    agent any
    stages{
        stage('Print Webhook Payload'){
            steps{
            script{
                echo "Webhook Payload: ${$.pull_request}"
            }
            }
        }
        
    }
}