# Cloud API Monitoring System 🚀

A cloud-style backend monitoring system built with FastAPI, Prometheus, Grafana, and Docker Compose.
This project demonstrates API development, structured logging, metrics collection, observability, and containerized deployment.

---

## 🧱 Tech Stack

* FastAPI — REST API backend
* Prometheus — Metrics collection and monitoring
* Grafana — Real-time dashboard visualization
* Docker & Docker Compose — Containerization and orchestration
* Python Logging — Structured application logs

---

## ✨ Features

* REST API with CRUD operations
* Structured logging system
* `/metrics` endpoint for Prometheus
* Real-time monitoring dashboards
* Request count tracking
* Error rate monitoring
* Response time / latency monitoring
* Dockerized multi-service deployment

---

## 📡 API Endpoints

| Endpoint      | Method | Description        |
| ------------- | ------ | ------------------ |
| `/health`     | GET    | Health check       |
| `/users`      | GET    | Retrieve users     |
| `/users`      | POST   | Create user        |
| `/users/{id}` | DELETE | Delete user        |
| `/metrics`    | GET    | Prometheus metrics |

---

## 🚀 Quick Start

Clone the repository:

```bash
git clone <your-repo-url>
cd <your-project-folder>
```

Run the full system:

```bash
docker compose up --build
```

---

## 📊 Monitoring Services

| Service     | URL                   |
| ----------- | --------------------- |
| FastAPI API | http://localhost:8000 |
| Prometheus  | http://localhost:9090 |
| Grafana     | http://localhost:3000 |

---

## 🏗️ System Architecture

```text
FastAPI API
     ↓
Structured Logging + Metrics
     ↓
Prometheus Monitoring
     ↓
Grafana Dashboard Visualization
```

---

## 📈 Grafana Dashboards

The Grafana dashboard includes:

* Requests per second
* Error rate monitoring
* API latency visualization
* Real-time metrics tracking

---

## 🎯 Learning Objectives

This project was built to practice:

* Backend API development
* Observability concepts
* Metrics monitoring
* Docker containerization
* Service orchestration
* Cloud engineering fundamentals

---

flowchart LR

%% =========================
%% USER LAYER
%% =========================
User[User / Client]

%% =========================
%% APPLICATION LAYER
%% =========================
subgraph APP[FastAPI Application]
direction TB

API[FastAPI Server]

H[Health Endpoint /health]
USR[User CRUD API /users]

STORE[In-Memory Data Store]

LOG[Logging System]
MET[Metrics System]

API --> H
API --> USR
API --> STORE
API --> LOG
API --> MET
end

%% =========================
%% OBSERVABILITY LAYER
%% =========================
subgraph OBS[Observability Stack]
direction TB

PROM[Prometheus - Metrics Collector]
GRAF[Grafana - Dashboard Visualization]

PROM --> GRAF
end

%% =========================
%% DEPLOYMENT LAYER
%% =========================
subgraph DEPLOY[Docker Compose Runtime]
direction TB

API_C[FastAPI Container]
PROM_C[Prometheus Container]
GRAF_C[Grafana Container]
end

%% =========================
%% FLOW (REAL SYSTEM BEHAVIOR)
%% =========================

User --> API

API --> LOG
API --> MET

API -->|exposes /metrics| PROM
PROM -->|scrapes metrics| API

GRAF -->|queries Prometheus| PROM

%% =========================
%% CONTAINER MAPPING (NO DUPLICATION)
%% =========================

API --- API_C
PROM --- PROM_C
GRAF --- GRAF_C

