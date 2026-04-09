A minimal Flask web application built for learning containerization.

![](https://github.com/samsrajyt/github-actions-capstone/actions/workflows/health-check.yml/badge.svg) ![](https://github.com/samsrajyt/github-actions-capstone/actions/workflows/main-pipeline.yml/badge.svg)![](https://github.com/samsrajyt/github-actions-capstone/actions/workflows/pr-pipeline.yml/badge.svg) 

![Python](https://img.shields.io/badge/Python-3.14-blue)
![Flask](https://img.shields.io/badge/Flask-3.1.1-green)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ED)


## Tech Stack

| Component | Technology |
|-----------|------------|
| Framework | Flask 3.1.1 |
| Runtime   | Python 3.14 |
| Container | Docker (python-slim / distroless) |


## Project Structure

```
flask-app-ecs/
├── app.py                 # Flask app with routes
├── run.py                 # Entry point (host 0.0.0.0, port 80)
├── requirements.txt       # Python dependencies
├── templates/
│   └── index.html         # Landing page
├── Dockerfile             # Simple single-stage build
```

## Endpoints

| Route     | Method | Description                     |
|-----------|--------|---------------------------------|
| `/`       | GET    | Landing page                    |
| `/health` | GET    | Health check (returns `Server is up and running`) |


## Quick Start

### Run locally

```bash
pip install -r requirements.txt
python run.py
```

App runs at **http://localhost:80**.

### Run with Docker

**Simple build:**

```bash
docker build -t flask-app .
docker run -p 80:80 flask-app
```
