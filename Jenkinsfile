pipeline {
  environment {
    registry = "jamesdidit72/account-generation"
    registryCredential = "docker_auth"
    dockerImage = ''
  }

  agent any

  options {
    skipStagesAfterUnstable()
  }

  stages {
    stage('Clone from Git') {
    		steps {
            git branch: 'main',
            url: 'https://github.com/kaiwolff/Account_Generation_Project.git'
    		}
    }

    stage('Build') {
      agent {
          docker {
              image 'python:3'
          }
      }
      steps {
          sh './build.sh'
          stash(name: 'compiled-results', includes: 'Account-Generator/.py*')
      }
    }

    stage('Test access rights') {
    	agent {
    			docker {
    					image 'qnib/pytest'
    			}
    	}
    	steps {
    			sh 'py.test --junit-xml test-reports/results_access_rights.xml Account-Generator/test_access_rights.py'
    	}
    	post {
    			always {
    					junit 'test-reports/results.xml'
    			}
    	}
    }
    stage('Test account deletion') {
    	agent {
    			docker {
    					image 'qnib/pytest'
    			}
    	}
    	steps {
    			sh 'py.test --junit-xml test-reports/results_acc_deletion.xml Account-Generator/test_account_deletion.py'
    	}
    	post {
    			always {
    					junit 'test-reports/results.xml'
    			}
    	}
    }
    stage('Test account management') {
    	agent {
    			docker {
    					image 'qnib/pytest'
    			}
    	}
    	steps {
    			sh 'py.test --junit-xml test-reports/results_acc_management.xml Account-Generator/test_account_management.py'
    	}
    	post {
    			always {
    					junit 'test-reports/results.xml'
    			}
    	}
    }
    stage('Test password control') {
    	agent {
    			docker {
    					image 'qnib/pytest'
    			}
    	}
    	steps {
    			sh 'py.test --junit-xml test-reports/results.xml Account-Generator/test_password_control.py'
    	}
    	post {
    			always {
    					junit 'test-reports/results.xml'
    			}
    	}
    }
    stage('Test password response') {
    	agent {
    			docker {
    					image 'qnib/pytest'
    			}
    	}
    	steps {
    			sh 'py.test --junit-xml test-reports/results.xml Account-Generator/test_password_response.py'
    	}
    	post {
    			always {
    					junit 'test-reports/results.xml'
    			}
    	}
    }

    stage('Build-Image') {
    	steps{
    			script {
    			dockerImage = docker.build registry + ":$BUILD_NUMBER"
    			}
    	}
    }

    stage('Deploy Image') {
    	steps{
    			script {
    					docker.withRegistry( '', registryCredential ) {
    							dockerImage.push()
    					}
    			}
    	}
    }

    stage('Remove Unused docker image') {
    	steps{
    			sh "docker rmi $registry:$BUILD_NUMBER"
    	}
    }
  }
}
