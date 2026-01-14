# HR ATTRITION ML SYSTEM — END-TO-END MLOPS PROJECT

## PROJECT OVERVIEW

This project implements a full production-style Machine Learning system
to predict employee attrition using the IBM HR Analytics dataset.

The goal was NOT just to train a model, but to design, build, and wire
an end-to-end ML system covering:
• experimentation
• model selection
• model registry
• backend inference
• frontend consumption
• database logging
• containerization
• CI/CD automation
• cloud-ready deployment design

This mirrors how real ML systems are built in industry.


## PROBLEM STATEMENT

Employee attrition is a critical business problem.
The task is to predict whether an employee is likely to leave the company
based on demographic, role-based, compensation, and satisfaction features.

This is formulated as a binary classification problem.


## DATASET

Dataset: IBM HR Analytics Attrition Dataset (Kaggle)

Target Variable:
• Attrition (Yes / No)

Feature Categories:
• Demographics (Age, Gender, Marital Status)
• Job & Role (Department, Job Role, Job Level)
• Compensation (Monthly Income, Stock Options, Salary Hike)
• Work Conditions (Overtime, Business Travel, Distance)
• Satisfaction & Performance
• Experience & Tenure

All features were analyzed for:
• data type
• cardinality
• distribution
• suitability for encoding and scaling


## STAGE 1 — DATA UNDERSTANDING & FEATURE DESIGN

• Clear separation of numerical and categorical features
• Validation of feature ranges and constraints
• Explicit handling of ordinal vs nominal variables
• Schema-first thinking to ensure consistency across:
  training → inference → UI → database


## STAGE 2 — PREPROCESSING PIPELINES

A production-ready preprocessing pipeline was built using:
• Numerical pipeline:
  – median imputation
  – standard scaling
• Categorical pipeline:
  – mode imputation
  – one-hot encoding
• ColumnTransformer to ensure deterministic feature ordering

The preprocessing pipeline is bundled with the model to guarantee
training-serving parity.


## STAGE 3 — MODEL EXPERIMENTATION

Multiple classification models were trained and evaluated under a
single MLflow experiment:

• Logistic Regression (baseline)
• Logistic Regression with L2 regularization
• Random Forest (baseline)

Each model was evaluated using:
• Accuracy
• Precision
• Recall
• F1 Score
• ROC-AUC

Emphasis was placed on understanding metric trade-offs,
especially under class imbalance.


## STAGE 4 — EXPERIMENT TRACKING (MLFLOW)

MLflow was used to track:
• parameters
• metrics
• artifacts
• preprocessing + model pipeline

Multiple runs per model were logged under the same experiment to enable
human-driven comparison and selection.

This allows reproducibility and transparent decision-making.


## STAGE 5 — MODEL REGISTRY & VERSIONING

The selected model was registered in the MLflow Model Registry.

Key practices:
• Explicit model versioning
• Alias-based loading (e.g., Production)
• Decoupling training from inference
• No hard-coded model paths

The backend always loads the model via registry alias,
making model upgrades non-breaking.


## STAGE 6 — BACKEND INFERENCE SERVICE

A FastAPI backend was built to serve predictions.

Key design principles:
• Schema-driven validation using Pydantic
• Strict input constraints to prevent silent failures
• Centralized model loading at startup
• Health endpoint exposing model metadata
• Latency measurement per request

The backend exposes:
• /health → service & model status
• /predict → inference endpoint


## STAGE 7 — DATABASE LOGGING (POSTGRESQL)

A PostgreSQL database is used to log prediction metadata.

Each inference logs:
• timestamp
• input payload
• prediction
• probability
• latency
• model name and alias

SQLAlchemy ORM is used for:
• table definition
• session management
• transaction safety

This enables observability and post-deployment analysis.


## STAGE 8 — FRONTEND (STREAMLIT)

A Streamlit UI was built to act as a client to the backend.

Design goals:
• Clean user input flow
• Controlled value ranges
• No business logic in UI
• API-first interaction

The UI:
• collects employee attributes
• sends request to backend
• displays prediction and confidence
• handles validation and errors gracefully


## STAGE 9 — CONTAINERIZATION

The system is fully containerized using Docker.

Services:
• FastAPI backend container
• Streamlit UI container
• PostgreSQL container (local)

Principles followed:
• Stateless containers
• No secrets baked into images
• Runtime configuration via environment variables
• Identical behavior across environments


## STAGE 10 — CI/CD PIPELINE

A GitHub Actions pipeline automates:

• Docker image builds
• Versioned tagging (latest, version, commit SHA)
• Secure authentication with Docker Hub
• Automatic image publishing on push to main

This enables reproducible, automated delivery without manual steps.


## DEPLOYMENT STATUS

• Backend, frontend, and database are cloud-ready
• Managed PostgreSQL tested on cloud provider
• Docker-based deployment validated
• CI/CD pipeline operational

Final deployment was intentionally paused after validation
due to free-tier limitations, while preserving full
production-grade architecture.


## KEY ENGINEERING TAKEAWAYS

• Training and serving are fully decoupled
• Model upgrades do not require code changes
• Schema validation prevents silent data issues
• Observability is built into the system
• Environment-agnostic configuration is enforced
• The system mirrors real industry ML stacks


## TECHNOLOGIES USED

• Python
• Scikit-learn
• MLflow
• FastAPI
• Pydantic
• PostgreSQL
• SQLAlchemy
• Streamlit
• Docker
• GitHub Actions


