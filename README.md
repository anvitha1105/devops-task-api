# DevOps Task Manager API

A simple DevOps-enabled Task Management REST API built using Flask, Docker, and GitHub Actions.

This project demonstrates:

* REST API development using Flask
* Docker containerization
* CI/CD automation using GitHub Actions
* Automated Docker image builds and pushes to Docker Hub

---

# Features

* Create tasks
* View all tasks
* Delete tasks
* Lightweight REST API
* Dockerized application
* Automated CI/CD pipeline

---

# Tech Stack

* Python 3.9
* Flask
* Docker
* GitHub Actions
* Docker Hub

---

# Project Structure

```bash
.
├── app.py
├── Dockerfile
├── requirements.txt
├── .github
│   └── workflows
│       └── main.yml
└── README.md
```

---

# API Endpoints

## Home Route

### GET /

Returns API status.

Response:

```bash
DevOps Task Manager API Running
```

---

## Get All Tasks

### GET /tasks

Returns all tasks.

Example Response:

```json
[
  {
    "id": 1,
    "task": "Learn Docker",
    "status": "pending"
  }
]
```

---

## Create Task

### POST /tasks

Request Body:

```json
{
  "task": "Learn CI/CD"
}
```

Example Response:

```json
{
  "id": 1,
  "task": "Learn CI/CD",
  "status": "pending"
}
```

---

## Delete Task

### DELETE /tasks/<task_id>

Example:

```bash
DELETE /tasks/1
```

Response:

```json
{
  "message": "task deleted"
}
```

---

# Running the Project Locally

## Clone Repository

```bash
git clone <your-repository-url>
cd devops-task-api
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Flask Application

```bash
python app.py
```

Application runs on:

```bash
http://localhost:5000
```

---

# Docker Setup

## Build Docker Image

```bash
docker build -t devops-task-api .
```

---

## Run Docker Container

```bash
docker run -p 5000:5000 devops-task-api
```

Application will run on:

```bash
http://localhost:5000
```

---

# CI/CD Pipeline

The project includes a GitHub Actions workflow that automatically:

* Checks out the repository
* Builds the Docker image
* Pushes the image to Docker Hub

The pipeline is triggered whenever code is pushed to the `main` branch.

---

# GitHub Actions Workflow

```yaml
name: Build and Push Docker Image

on:
  push:
    branches: ["main"]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v3

      - name: Login to Docker Hub
        run: echo "${{ secrets.DOCKER_PASSWORD }}" | docker login -u "${{ secrets.DOCKER_USERNAME }}" --password-stdin

      - name: Build Docker Image
        run: docker build -t ${{ secrets.DOCKER_USERNAME }}/devops-task-api .

      - name: Push Docker Image
        run: docker push ${{ secrets.DOCKER_USERNAME }}/devops-task-api
```

---

# Future Improvements

* Add database integration (PostgreSQL/MySQL)
* Deploy using Kubernetes
* Add authentication and authorization
* Integrate monitoring tools
* Add unit and integration testing
* Implement Swagger/OpenAPI documentation
* Add Terraform for infrastructure automation

---

# Learning Outcomes

This project helped in understanding:

* REST API development
* Docker containerization
* CI/CD pipeline automation
* GitHub Actions workflows
* DevOps deployment practices

---

# Author

Anvitha N
