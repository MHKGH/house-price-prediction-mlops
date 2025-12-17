# 🏠 House Price Prediction MLOps Pipeline

A comprehensive End-to-End MLOps project that demonstrates the lifecycle of a Machine Learning model from training to production deployment.

## 🚀 Project Overview
This project builds a Linear Regression model to predict house prices based on size and number of bedrooms. It focuses on the **Operational (Ops)** side of Machine Learning, including:
* **Data Engineering:** Synthetic data generation using Pandas.
* **Model Training:** Scikit-Learn training pipeline.
* **Serving:** REST API development using **FastAPI**.
* **Containerization:** Packaging the application with **Docker**.
* **Orchestration:** Deploying to a local **Kubernetes** cluster.

## 🛠️ Tech Stack
* **Language:** Python 3.9
* **ML Library:** Scikit-Learn
* **API Framework:** FastAPI
* **Container:** Docker
* **Orchestration:** Kubernetes (Minikube)

---

## 💻 How to Run Locally

### 1. Clone the Repository
```bash
git clone [https://github.com/MHKGH/house-price-prediction-mlops.git](https://github.com/MHKGH/house-price-prediction-mlops.git)
cd house-price-prediction-mlops
2. Run with Docker (Easiest Method)
Make sure Docker is installed and running.

Bash

# Build the image
docker build -t house-predictor:v2 .

# Run the container
docker run -d -p 8000:8000 --name house-app house-predictor:v2
3. Test the API
Open your browser to the automatically generated Swagger UI: 👉 http://localhost:8000/docs

Or test via terminal:

Bash

curl -X POST "[http://127.0.0.1:8000/predict](http://127.0.0.1:8000/predict)" \
     -H "Content-Type: application/json" \
     -d '{"size_sqft": 2500, "bedrooms": 3}'
☸️ How to Deploy on Kubernetes
If you have Minikube installed, you can simulate a production deployment.

Bash

# 1. Load image into Minikube
minikube image load house-predictor:v2

# 2. Apply Manifests
kubectl apply -f k8s-deployment.yaml

# 3. Check Status
kubectl get pods

# 4. Get Access URL
minikube service house-app-service --url
📂 Project Structure
├── data/               # Raw training data
├── models/             # Serialized model artifacts (.pkl)
├── src/
│   ├── app.py          # FastAPI application (Serving)
│   ├── train.py        # Model training script
│   └── generate_data.py # Data generation script
├── Dockerfile          # Container instructions
├── k8s-deployment.yaml # Kubernetes manifests
└── requirements.txt    # Python dependencies