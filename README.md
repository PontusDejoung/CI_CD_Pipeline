# CI/CD Pipeline with kind and Kubernetes

This project demonstrates a simple CI/CD pipeline that builds, tests, and deploys a Flask application to a local Kubernetes cluster using kind.

## Features
- Dockerized Flask application
- Deployment to Kubernetes (kind)
- GitHub Actions for CI/CD

## Prerequisites
- Docker
- kind
- kubectl
- GitHub Actions

## Usage
1. Clone this repository.
2. Start a kind cluster:
   ```bash
   kind create cluster
