# ai-model-deployment-aws-
Deployed a machine learning model for real-time prediction using AWS Lambda and API Gateway.
# AI Model Deployment on AWS

This project demonstrates how to deploy a simple machine learning model to AWS Lambda, expose it through API Gateway, and automate deployments using GitHub Actions.

## Key Features
- Train a lightweight Linear Regression model using Scikit-learn.
- Deploy the model as an AWS Lambda function.
- Access predictions via a REST API (API Gateway).
- Automate packaging and deployment through GitHub Actions.

## Technologies Used
- AWS Lambda
- AWS API Gateway
- GitHub Actions
- Python, Scikit-learn, NumPy
- OpenAPI 3.0 Specification

## How It Works
1. Train a simple machine learning model and save it as `model.pkl`.
2. Package the model and Lambda handler together.
3. Deploy the package to AWS Lambda using an automated workflow.
4. Call the `/predict` endpoint with an input value to get real-time predictions.

## Status
This project is a simplified proof-of-concept for cloud-based machine learning deployment.

## Author
- Mahee Shah ([GitHub Profile](https://github.com/maheeashah))
