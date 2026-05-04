build:
	docker build -t mlops-flask-app .

run:
	docker run -p 8080:8080 mlops-flask-app

push:
	docker tag mlops-flask-app:latest <aws_account_id>.dkr.ecr.us-east-1.amazonaws.com/mlops-flask-app:latest
	docker push <aws_account_id>.dkr.ecr.us-east-1.amazonaws.com/mlops-flask-app:latest
	