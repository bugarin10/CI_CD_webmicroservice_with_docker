[![Python application test with Github Actions](https://github.com/bugarin10/CI_CD_webmicroservice_with_docker/actions/workflows/main.yml/badge.svg)](https://github.com/bugarin10/CI_CD_webmicroservice_with_docker/actions/workflows/main.yml)

Below is a README.md guide for your repository, emphasizing the CI/CD process and explaining the components of your Flask application and Docker setup:

---

# Embedder App

## Overview

This repository contains a Flask application named "Embedder" that processes text inputs, splits them into chunks, computes embeddings for each chunk, and returns the processed data in JSON format. Additionally, it includes a Docker setup for containerization and a GitHub Actions workflow for Continuous Integration and Continuous Deployment (CI/CD).

## Components

### Flask Application

The main file of the Flask application is `app.py`, which defines the following functionalities:

- Receives a POST request at the endpoint `/process_text`.
- Processes the text input by splitting it into chunks and computing embeddings for each chunk.
- Returns the processed data in JSON format.

### Payload Example

You can test the Flask application using the following payload with curl:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"text": "Hello world!"}' http://127.0.0.1:5000/process_text
```

### Docker Setup

The `Dockerfile` sets up the Docker environment for the Flask application. It installs necessary packages, sets the working directory, copies application files, installs dependencies, exposes port 5000, and specifies the command to run the Flask app.

### GitHub Actions Workflow (CI/CD)

The `main.yml` file defines the GitHub Actions workflow for CI/CD. It consists of the following steps:

1. Sets up the Python environment with version 3.10.
2. Installs project dependencies.
3. Lints the code using pylint.
4. Formats the code using black.
5. Builds the Docker image.
6. Pushes the Docker image to DockerHub.

## CI/CD Emphasis

The CI/CD process ensures that changes to the codebase are tested, linted, and formatted automatically. It also automates the Docker image build and pushes it to DockerHub, enabling seamless deployment and version control.

## Makefile

The `Makefile` simplifies common development tasks with the following commands:

- `venv`: Sets up a virtual environment.
- `install`: Installs project dependencies.
- `format`: Formats the code using black.
- `lint`: Lints the code using pylint.
- `docker`: Builds the Docker image.

## Usage

To run the Flask application locally, ensure you have Python 3.10 and the required dependencies installed. Then, follow these steps:

1. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
2. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
3. Install project dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the Flask app:
   ```bash
   python app.py
   ```

For Docker usage, ensure Docker is installed on your machine and run the following commands:

1. Build the Docker image:
   ```bash
   make docker
   ```
2. Run the Docker container:
   ```bash
   docker run -p 5000:5000 bugarin10/embedder:latest
   ```
