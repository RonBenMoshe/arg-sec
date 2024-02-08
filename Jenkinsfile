properties(
    [parameters([
        choice(name: 'StageToRun',choices: ['Build', 'Deploy'], description: 'Choose the stage to run when running the pipeline manually'),
        string(name: 'sha1', description: 'branch to build from',defaultValue: 'refs/heads/main')
    ])])
pipeline{
    agent any
    triggers {
        cron 'H 17 * * *'
    }
    stages{
        stage('Build'){
            when {
                anyOf {
                    expression {
                        params.StageToRun == 'Build' && currentBuild.buildCauses.toString().contains('UserIdCause')
                    }
                    expression {
                        currentBuild.buildCauses.toString().contains('GhprbCause')
                    }
                
                }
            }
            steps{
                script{
                    echo currentBuild.buildCauses.toString()
                    echo "Files:"
                    sh "ls -la"
                    if(ghprbPullId.isEmpty()){
                        ghprbPullId = "manual"
                    }
                    sh """
                        docker build -t 161192472568.dkr.ecr.us-east-1.amazonaws.com/ron-ben.moshe:${ghprbPullId} .
                        mkdir -p data
                        docker run -v data:/tmp 161192472568.dkr.ecr.us-east-1.amazonaws.com/ron-ben.moshe:${ghprbPullId}
                        ls /data
                        docker tag 161192472568.dkr.ecr.us-east-1.amazonaws.com/ron-ben.moshe:${ghprbPullId} 161192472568.dkr.ecr.us-east-1.amazonaws.com/ron-ben.moshe:latest
                    """
                    withAWS(credentials: 'Aws', region: 'us-east-1') {
                        sh """
                        aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 161192472568.dkr.ecr.us-east-1.amazonaws.com
                        docker push -a 161192472568.dkr.ecr.us-east-1.amazonaws.com/ron-ben.moshe
                        aws s3 cp /data/test.txt s3://ron-ben.moshe/pr_${ghprbPullId}.txt
                        """
                    }
                }
            }
        }
        stage('Deploy'){
            when {
                anyOf {
                    expression {
                        params.StageToRun == 'Deploy' && currentBuild.buildCauses.toString().contains('UserIdCause')
                    }
                    expression {
                        currentBuild.buildCauses.toString().contains('TimerTriggerCause')
                    }
                
                }
            }
            steps{
                script{
                    echo currentBuild.buildCauses.toString()
                    withAWS(credentials: 'Aws', region: 'us-east-1') {
                        sh """
                        latest=\$(aws s3 ls s3://ron-ben.moshe/ --recursive | sort | tail -n 1 | awk '{print \$4}')
                        aws s3 cp s3://ron-ben.moshe/\$latest test.txt
                        [[ -s test.txt ]] && cat /tmp/test.txt || echo "File Empty"
                        """
                    }
                }
            }
        }

        
    }
}
