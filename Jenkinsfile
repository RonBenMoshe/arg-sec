pipeline{
    agent any
    stages{
        stage('Print Webhook Payload'){
            steps{
            script{
                echo "Webhook Payload: ${GITHUB_PR_NUMBER}"
                echo "Test"
            }
            }
        }
        
    }
}
