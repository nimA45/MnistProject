pipeline {
    agent any
    
    stages {
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
	    stage(' Compare Accurary and merge or not'){
		    steps{
			    sh stage('Compare Accuracy and merge or not') {
    steps {
        sh '''
            if [ "$(head -n 1 fashion-mnist-train-2.csv_accuracy.txt)" -gt "$(head -n 1 fashion-mnist-train-1.csv_accuracy.txt)" ]; then
                /Users/nima/miniconda3/bin/python -c "print('yes')"
            fi
        '''
    }
}

		    }
	    }
        
    }
}
