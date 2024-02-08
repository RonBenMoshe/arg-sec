properties(
    [parameters([
        choice(name: 'StageToRun',choices: ['Build', 'Deploy'], description: 'Choose the stage to run when running the pipeline manually')
    ])])
pipeline{
    agent any
    triggers {
        cron 'H 17 * * *'
        githubPullRequests events: [Open(), commitChanged()], spec: '', triggerMode: 'HEAVY_HOOKS'
    }
    stages{
        stage('Build'){
            when {
                anyOf {
                    expression {
                        params.StageToRun == 'Build' && currentBuild.buildCauses.toString().contains('UserIdCause')
                    }
                    expression {
                        currentBuild.buildCauses.toString().contains('GitHubPRCause')
                    }
                
                }
            }
            steps{
                script{
                    echo currentBuild.buildCauses.toString()
                    echo "Files:"
                    sh "ls -la"
                    sh """
                        docker build -t 161192472568.dkr.ecr.us-east-1.amazonaws.com/ron-ben.moshe:${GITHUB_PR_NUMBER} .
                        mkdir -p data
                        docker run -v data:/tmp 161192472568.dkr.ecr.us-east-1.amazonaws.com/ron-ben.moshe:${GITHUB_PR_NUMBER}
                        ls /data
                        docker tag 161192472568.dkr.ecr.us-east-1.amazonaws.com/ron-ben.moshe:${GITHUB_PR_NUMBER} 161192472568.dkr.ecr.us-east-1.amazonaws.com/ron-ben.moshe:latest

                    """
                }
            }
        }

        
    }
}