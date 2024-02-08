pipeline{
    agent any
    stages{
        stage('Build'){
            steps{
                script{
                    echo currentBuild.buildCauses.toString()
                    echo "Files:"
                    sh "ls -la"
                    sh """
                        docker build -t 161192472568.dkr.ecr.us-east-1.amazonaws.com/ron-ben.moshe:${GITHUB_PR_NUMBER}
                        docker tag 161192472568.dkr.ecr.us-east-1.amazonaws.com/ron-ben.moshe:${GITHUB_PR_NUMBER} 161192472568.dkr.ecr.us-east-1.amazonaws.com/ron-ben.moshe:latest
                    """
                }
            }
        }

        
    }
}