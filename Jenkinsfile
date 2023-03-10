node{
    stage("SCM Checkout"){
        checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'Github-Username-Password', url: 'https://github.com/imhetvi/FlaskDockerJenkins.git']])    
	}
    stage("docker build"){
		script{
			bat "docker build -t flask-app:1.0 -f Dockerfiles/Dockerfile.multistage ."
		}
    }
	stage("docker run"){
		script{
			bat "docker run -it -d -p 5000:5000 --name flask-app-cont flask-app:1.0"
		}
	}
}

