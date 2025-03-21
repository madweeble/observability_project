# Observability Demo

## Python Microservices with FastAPI, Docker/Minikube, and Istio

## Overview
Deploys a simple FastAPI microservice on Minikube with Istio as the service mesh.
Initial setup is done using Docker to build and run services.
Configures observability using Prometheus, Grafana, and Jaeger to collect metrics, logs, and traces.

## Tech Stack
- FastAPI: Lightweight Python framework for building APIs.
- Docker: Docker used initially to build and test services.
- Minikube: Local Kubernetes cluster for testing.
- Istio: Service mesh for traffic control and observability.
- Prometheus: Metrics collection system.
- Grafana: Visualization tool for monitoring.
- Jaeger: Distributed tracing system.

---

## Step 1: Setup Minikube and Istio

Start Minikube:
```bash
minikube start --cpus=4 --memory=8192
```

Download and Install Istio:
```bash
curl -L https://istio.io/downloadIstio | ISTIO_VERSION=1.21.0 sh -
cd istio-1.21.0
export PATH=$PWD/bin:$PATH
istioctl install --set profile=demo -y
```

Enable automatic sidecar injection for the default namespace:
```bash
kubectl label namespace default istio-injection=enabled
```

## Step 2: Deploy FastAPI Microservice

Apply the deployment:
```bash
kubectl apply -f fastapi-deployment.yaml
```
## Step 3: Expose FastAPI via Istio Gateway

Apply the gateway configuration:
```bash
kubectl apply -f istio-gateway.yaml
```
