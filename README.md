# NLP-WEB-APP
AWS-CI/CD-Deployment-with-Github-Actions

1. Login to AWS console.
2. Create IAM user for deployment
#with specific access

    1. EC2 access : It is virtual machine

    2. ECR: Elastic Container registry to save your docker image in aws
    - Search IAM-- Go to users---Create Users--Give username--Attach Policies directly--
    #Policy:

    1. AmazonEC2ContainerRegistryFullAccess

    2. AmazonEC2FullAccess
    --Add tag (Optional)
    Create access Key and download the CSV
3. Create ECR repo to store/save docker image
    search ECR under services--Create a Repo--Give Project Name
    copy URI :something.dkr.ecr.something.amazonaws.com/nlp-app

4. Create EC2 machine (Ubuntu)
    Search EC2 under Services--launch instance--give name--select ubuntu--and version--select instance type as per need--key value pair--create instance and connect

5. Open EC2 and Install docker in EC2 Machine:
#optinal

sudo apt-get update -y

sudo apt-get upgrade

#required

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker

# to check docker version 
docker --version

6. Configure EC2 as self-hosted runner: Go to your Github Repo-->
setting>actions>runner>new self hosted runner> choose os> then run command one by one

7. Setup github secrets: Github repo--Settings--secrets and variable--Action--New repo secrets

AWS_ACCESS_KEY_ID=

AWS_SECRET_ACCESS_KEY=

AWS_REGION = eu-north-1

AWS_ECR_LOGIN_URI = something.dkr.ecr.something.amazonaws.com

ECR_REPOSITORY_NAME = nlp-app






