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
        script {
        	def file1 = readFile('fashion-mnist-train-1.csv_accuracy.txt').trim().toDouble()
		def file2 = readFile('fashion-mnist-train-2.csv_accuracy.txt').trim().toDouble()

		if (file2 > file1) {
		    sh 'git checkout main'
		    sh 'git merge release'
		} else {
		    sh 'git branch -D release'
		}
	}

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

	
