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
          stash(name: 'compiled-results', includes: 'Account-Generator/*.py*')
      }
    }

    stage('Test access rights') {
    	agent {
    			docker {
    					image 'qnib/pytest'
    			}
    	}
    	steps {
    			sh './test_access_rights.sh'
    	}
    	post {
    			always {
    					junit 'test-reports/results_access_rights.xml'
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
    			sh './test_account_deletion.sh'
    	}
    	post {
    			always {
    					junit 'test-reports/results_acc_deletion.xml'
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
    			sh './test_account_management.sh'
    	}
    	post {
    			always {
    					junit 'test-reports/results_acc_management.xml'
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
    			sh './test_password_control.sh'
    	}
    	post {
    			always {
    					junit 'test-reports/results_password_control.xml'
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
    			sh './test_password_response.sh'
    	}
    	post {
    			always {
    					junit 'test-reports/results_password_response.xml'
    			}
    	}
    }
    stage('Test password check strength') {
    	agent {
    			docker {
    					image 'qnib/pytest'
    			}
    	}
    	steps {
    			sh './test_password_check_strength.sh'
    	}
    	post {
    			always {
    					junit 'test-reports/test_password_check_strength.xml'
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
