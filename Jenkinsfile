pipeline{
    agent{
        any
    }
    stages{
        stage('Print Webhook Payload'){
            script{
                echo "Webhook Payload: ${$.pull_request}"
            }
        }
        
    }
}