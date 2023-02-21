pipeline {
    agent any
    
    stages {
	    stage('Check and Delete Release Branch') {
	steps {
	sh 'if git show-ref --verify --quiet refs/heads/release; then git branch -D release; fi'
	}
	}

	stage('Create Release Branch') {
		steps {
	sh 'git checkout -b release'
		}
	}
	    stage('Train new model '){
		    steps{
		    sh '/Users/nima/miniconda3/bin/python model.py fashion-mnist-train-2.csv'
		    }
	    }
	stage('Compare and Merge Release Branch') {
    steps {
		sh """
			file1=\$(cat fashion-mnist-train-1.csv_accuracy.txt | tr -d '[:space:]')
			file2=\$(cat fashion-mnist-train-2.csv_accuracy.txt | tr -d '[:space:]')

			if [ "\$file2" '>' "\$file1" ]; then
			    git checkout main
			    git merge release
			else
			    git branch -D release
			fi
		"""
    }
}


	    
        stage('Build') {

			steps {
				sh 'docker build -t mnistmlops .'
			}
		}
        stage('Run Docker image and test') {
            steps {
                sh 'docker run -p 5000:5000 -d mnistmlops'
            }
        }
        stage ('Test App'){
            steps{
                sh '/Users/nima/miniconda3/bin/python test.py'
            }
        }
	    
	    
    }
}
