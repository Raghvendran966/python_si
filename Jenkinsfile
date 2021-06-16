pipeline {
    agent any 
    stages{
        stage('checkout'){
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/Raghvendran966/python_si.git']]])
            }
        }
        stage('buiding'){
            steps {
                sh 'docker build -t sampleapp:latest .'
                sh 'docker tag sampleapp raghvendran966/sampleapp:latest'
                sh 'docker tag sampleapp raghvendran966/sampleapp:$BUILD_NUMBER'
            
            }
        }
        stage('deploying image')
        {
            steps {
                withDockerRegistry([ credentialsId: "dockerhub", url: "" ]){
                    sh  'docker push raghvendran966/sampleapp:latest'
                    sh  'docker push raghvendran966/sampleapp:$BUILD_NUMBER' 
                }
            }
        }
        
    }
}
