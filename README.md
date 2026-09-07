# 🎯 AI Sales Lead Prediction & Analytics System

### 🚀 Machine Learning Powered Sales Intelligence Platform

**Predict. Prioritize. Analyze. Act.**

An end-to-end **AI/ML sales intelligence application** that predicts lead conversion probability, automatically prioritizes prospects, analyzes sales performance, and enables batch lead scoring through an interactive Streamlit dashboard.

<p align="center">

![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Application-FF4B4B?style=for-the-badge\&logo=streamlit\&logoColor=white)
![Scikit Learn](https://img.shields.io/badge/Scikit--Learn-ML-F7931E?style=for-the-badge\&logo=scikit-learn\&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Analytics-150458?style=for-the-badge\&logo=pandas\&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-Interactive%20Charts-3F4F75?style=for-the-badge\&logo=plotly\&logoColor=white)
![Joblib](https://img.shields.io/badge/Joblib-Model%20Persistence-2E8B57?style=for-the-badge)

</p>

<p align="center">

**AI-Powered Lead Scoring • Sales Analytics • Batch Prediction • Decision Support**

</p>

---

## 📌 Table of Contents

* [Overview](#-overview)
* [Why This Project](#-why-this-project)
* [Problem Statement](#-problem-statement)
* [Solution](#-solution)
* [Key Features](#-key-features)
* [Application Workflow](#-application-workflow)
* [System Architecture](#-system-architecture)
* [Machine Learning Pipeline](#-machine-learning-pipeline)
* [Input Features](#-input-features)
* [Lead Prioritization](#-lead-prioritization)
* [Application Modules](#-application-modules)
* [Technology Stack](#-technology-stack)
* [Project Structure](#-project-structure)
* [Installation](#-installation)
* [Configuration](#-configuration)
* [Running Locally](#-running-locally)
* [Model Usage](#-model-usage)
* [Model Evaluation](#-model-evaluation)
* [Batch Prediction](#-batch-prediction)
* [Testing](#-testing)
* [API Documentation](#-api-documentation)
* [Deployment](#-deployment)
* [Security](#-security)
* [Known Limitations](#-known-limitations)
* [Future Improvements](#-future-improvements)
* [Roadmap](#-roadmap)
* [Business Impact](#-business-impact)
* [Author](#-author)

---

# 🎯 Overview

**AI Sales Lead Prediction & Analytics System** is an end-to-end machine-learning application designed to transform historical sales data into actionable lead intelligence.

  Local URL: http://localhost:8501
  Network URL: http://192.168.1.38:8501

The platform allows sales teams to:

> **Understand → Predict → Prioritize → Take Action**

Instead of treating every lead equally, the system estimates the probability that a lead will convert and translates that probability into an actionable sales priority.

### Core capabilities

| Capability               | Description                                                |
| ------------------------ | ---------------------------------------------------------- |
| 🤖 Lead Prediction       | Predict conversion probability for individual leads        |
| 🔥 Lead Prioritization   | Categorize leads as HIGH, MEDIUM, or LOW priority          |
| 📊 Sales Analytics       | Analyze industry, lead source, budget, and sales behaviour |
| 📁 Batch Prediction      | Score multiple leads through CSV upload                    |
| 🧠 Model Information     | Display model name, features, and evaluation metrics       |
| 💡 Sales Recommendations | Generate recommended actions based on lead probability     |
| 📥 Result Export         | Download batch prediction results as CSV                   |
| 📝 Logging               | Track application and prediction events                    |

---

# 💼 Why This Project?

Traditional sales processes often depend heavily on manual lead evaluation.

When hundreds or thousands of leads are generated, sales representatives may struggle to determine:

* Which prospects deserve immediate attention?
* Which leads are likely to convert?
* Which marketing channels generate high-quality leads?
* Does faster response improve conversion?
* How does customer budget relate to conversion?
* How should sales resources be allocated?

This project addresses these challenges using **machine learning + interactive analytics**.

---

# 🚨 Problem Statement

> **Develop an intelligent sales lead prediction system that uses historical lead data to estimate conversion probability and help sales teams prioritize leads based on their likelihood of conversion.**

### Business challenge

```text
Large Number of Leads
        ↓
Manual Lead Evaluation
        ↓
Time Consuming
        ↓
Inconsistent Prioritization
        ↓
Missed High-Value Opportunities
```

### Proposed solution

```text
Historical Sales Data
        ↓
Machine Learning
        ↓
Conversion Probability
        ↓
Lead Priority
        ↓
Sales Recommendation
        ↓
Better Resource Allocation
```

---

# 💡 Solution

The system uses a trained classification model to analyze lead characteristics and calculate the probability of conversion.

The prediction is then converted into a business-friendly priority:

```text
                    LEAD
                      │
                      ▼
             ML Classification
                      │
                      ▼
          Conversion Probability
                      │
          ┌───────────┼───────────┐
          ▼           ▼           ▼
       ≥ 80%       50–79.99%      < 50%
          │           │           │
          ▼           ▼           ▼
        HIGH        MEDIUM        LOW
          │           │           │
          ▼           ▼           ▼
     Immediate     Structured    Automated
      Contact       Follow-up    Nurturing
```

---

# ✨ Key Features

## 🤖 1. Intelligent Lead Prediction

Enter lead information and receive:

* Conversion probability
* Binary prediction
* Sales priority
* AI-generated recommendation

Example:

```text
┌─────────────────────────────────────┐
│      LEAD PREDICTION RESULT         │
├─────────────────────────────────────┤
│ Conversion Probability   87.42%    │
│ Prediction               LIKELY     │
│ Sales Priority           HIGH 🔥    │
└─────────────────────────────────────┘
```

---

## 🔥 2. Automated Lead Prioritization

The system transforms ML probabilities into actionable business categories.

|        Score | Priority   | Sales Strategy                 |
| -----------: | ---------- | ------------------------------ |
|     🟢 ≥ 80% | **HIGH**   | Immediate personalized contact |
| 🟡 50–79.99% | **MEDIUM** | Structured follow-up           |
|     🔵 < 50% | **LOW**    | Automated nurturing            |

---

## 📊 3. Interactive Sales Dashboard

The dashboard provides high-level sales intelligence through:

* Total leads
* Converted leads
* Conversion rate
* Average budget
* Average follow-up count
* Industry conversion analysis
* Lead source performance
* Budget distribution
* Follow-up behaviour

Interactive charts are powered by **Plotly**.

---

## 📈 4. Advanced Sales Analytics

The application provides three analytical perspectives:

### Industry Analysis

Examines:

* Lead volume
* Conversion count
* Conversion rate
* Average budget
* Budget vs conversion relationship

### Lead Source Analysis

Identifies which lead sources produce stronger conversion performance.

### Sales Behaviour

Analyzes the relationship between first-response time and conversion outcome.

---

## 📁 5. Batch Prediction

Sales teams can upload a CSV containing multiple leads.

The application:

```text
Upload CSV
    ↓
Validate Schema
    ↓
Run Model
    ↓
Calculate Probabilities
    ↓
Generate Predictions
    ↓
Assign Priority
    ↓
Sort Leads
    ↓
Download Results
```

---

## 🧠 6. Model Information

The application displays:

* Selected model
* Model metrics
* Input features
* Data leakage prevention information

The model artifact is loaded dynamically using Joblib.

---

# 🖥️ Application Modules

The application contains five primary modules.

| Module               | Purpose                    |
| -------------------- | -------------------------- |
| 🏠 Dashboard         | Overall sales performance  |
| 🤖 Lead Prediction   | Individual lead scoring    |
| 📊 Sales Analytics   | Detailed business analysis |
| 📁 Batch Prediction  | Bulk lead scoring          |
| 🧠 Model Information | Model details and metrics  |

---

# 🔄 Application Workflow

```text
                       ┌─────────────────┐
                       │ Historical Data │
                       └────────┬────────┘
                                │
                                ▼
                       ┌─────────────────┐
                       │ Data Processing │
                       └────────┬────────┘
                                │
                                ▼
                       ┌─────────────────┐
                       │ Feature         │
                       │ Selection       │
                       └────────┬────────┘
                                │
                                ▼
                       ┌─────────────────┐
                       │ Model Training  │
                       └────────┬────────┘
                                │
                                ▼
                       ┌─────────────────┐
                       │ Model Evaluation│
                       └────────┬────────┘
                                │
                                ▼
                       ┌─────────────────┐
                       │ Joblib Artifact │
                       └────────┬────────┘
                                │
                                ▼
                    ┌────────────────────────┐
                    │ Streamlit Application   │
                    └────────────┬───────────┘
                                 │
             ┌───────────────────┼──────────────────┐
             ▼                   ▼                  ▼
        Dashboard           Prediction          Analytics
             │                   │                  │
             │                   ▼                  │
             │             Probability             │
             │                   │                  │
             │                   ▼                  │
             │              Priority               │
             │                   │                  │
             └───────────────────┼──────────────────┘
                                 │
                                 ▼
                        Business Decisions
```

---

# 🏗️ System Architecture

```text
┌─────────────────────────────────────────────────────────────┐
│                       USER INTERFACE                        │
│                         Streamlit                           │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Dashboard │ Prediction │ Analytics │ Batch │ Model Info  │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│                     APPLICATION LOGIC                       │
│                                                             │
│  Data Loading │ Validation │ Prediction │ Prioritization  │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│                     ML INFERENCE LAYER                      │
│                                                             │
│                 Trained Classification Model               │
│                         Joblib                              │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│                      DATA LAYER                             │
│                                                             │
│               Historical Sales CSV Dataset                 │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

# 🧠 Machine Learning Pipeline

The project follows a standard supervised machine-learning workflow.

```text
Raw Sales Data
      │
      ▼
Data Cleaning
      │
      ▼
Feature Engineering
      │
      ▼
Train / Test Split
      │
      ▼
Model Training
      │
      ▼
Model Evaluation
      │
      ▼
Best Model Selection
      │
      ▼
Joblib Serialization
      │
      ▼
Streamlit Inference
```

---

# 🎛️ Input Features

The current model uses six prediction features.

| Feature                | Type        | Description                |
| ---------------------- | ----------- | -------------------------- |
| `industry`             | Categorical | Business industry          |
| `service`              | Categorical | Requested service          |
| `lead_source`          | Categorical | Source of lead             |
| `budget_inr`           | Numerical   | Estimated customer budget  |
| `first_response_hours` | Numerical   | Time taken to respond      |
| `followup_count`       | Numerical   | Number of sales follow-ups |

### Target

```text
converted
```

The target represents whether the lead successfully converted.

---

# 🔥 Lead Scoring Logic

The application uses the predicted probability to determine business priority.

### High Priority

```python
probability >= 0.80
```

### Medium Priority

```python
0.50 <= probability < 0.80
```

### Low Priority

```python
probability < 0.50
```

The binary prediction threshold is:

```python
probability >= 0.50
```

---

# 💬 Recommendation Engine

The prediction is converted into an actionable sales recommendation.

```text
HIGH
 ↓
Immediate personalized follow-up

MEDIUM
 ↓
Structured sales follow-up

LOW
 ↓
Automated nurturing
```

This creates a bridge between:

> **Machine Learning Output → Business Decision**

---

# 🧰 Technology Stack

### Core

* Python
* Streamlit

### Machine Learning

* Scikit-learn
* Joblib

### Data

* Pandas
* CSV

### Visualization

* Plotly Express
* Plotly Graph Objects

### Application Engineering

* Python Logging
* Environment Variables
* Streamlit Caching
* Exception Handling

---

# 📂 Project Structure

```text
AI-Sales-Lead-Prediction-Analytics/
│
├── 📄 app.py
│
├── 📊 04_jzd_sales_data.csv
│
├── 🤖 models/
│   └── lead_conversion_model.joblib
│
├── 📓 notebooks/
│   └── model_training.ipynb
│
├── 🧪 tests/
│   └── test_app.py
│
├── 📝 logs/
│   └── app.log
│
├── 📦 requirements.txt
│
├── 🔒 .gitignore
│
└── 📖 README.md
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-Sales-Lead-Prediction-Analytics.git
```

```bash
cd AI-Sales-Lead-Prediction-Analytics
```

---

## 2️⃣ Create Virtual Environment

### Windows

```bash
python -m venv .venv
```

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv .venv
```

```bash
source .venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

If the requirements file does not exist:

```bash
pip install streamlit pandas plotly joblib scikit-learn
```

Generate it using:

```bash
pip freeze > requirements.txt
```

---

# ⚙️ Configuration

The application supports environment-based configuration.

## Dataset

Default:

```text
04_jzd_sales_data.csv
```

Override:

### Windows PowerShell

```powershell
$env:DATA_PATH="data/sales_data.csv"
```

### Linux/macOS

```bash
export DATA_PATH="data/sales_data.csv"
```

---

## Model

Default:

```text
models/lead_conversion_model.joblib
```

Override:

### Windows PowerShell

```powershell
$env:MODEL_PATH="models/my_model.joblib"
```

### Linux/macOS

```bash
export MODEL_PATH="models/my_model.joblib"
```

---

# ▶️ Running Locally

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will be available at:

```text
http://localhost:8501
```

---

# 🧪 Testing

Install pytest:

```bash
pip install pytest
```

Run the test suite:

```bash
pytest
```

Verbose mode:

```bash
pytest -v
```

### Recommended test coverage

```text
✓ Dataset loading
✓ Model loading
✓ Feature validation
✓ Prediction probability
✓ Prediction threshold
✓ Lead prioritization
✓ Batch CSV validation
✓ Batch prediction
✓ Output generation
✓ Error handling
```

---

# 🔌 API Documentation

The current application does **not expose a REST API**.

It uses Streamlit as the application interface.

However, the internal prediction interface follows a simple inference pattern.

### Input

```python
input_data = pd.DataFrame([
    {
        "industry": "Technology",
        "service": "AI Development",
        "lead_source": "Website",
        "budget_inr": 150000,
        "first_response_hours": 2,
        "followup_count": 3
    }
])
```

### Inference

```python
probability = model.predict_proba(
    input_data[FEATURES]
)[:, 1]
```

### Output

```text
Conversion Probability
Prediction
Lead Priority
Sales Recommendation
```

---

# 📦 Model Artifact

The application expects the Joblib file to contain a model artifact similar to:

```python
{
    "model": trained_model,

    "features": [
        "industry",
        "service",
        "lead_source",
        "budget_inr",
        "first_response_hours",
        "followup_count"
    ],

    "model_name": "Selected Model",

    "metrics": {
        "accuracy": 0.00,
        "precision": 0.00,
        "recall": 0.00,
        "f1_score": 0.00
    }
}
```

This approach keeps the application flexible because model configuration is stored alongside the trained model.

---

# 📈 Model Evaluation

The application can display model evaluation metrics stored in the Joblib artifact.

Common evaluation metrics include:

| Metric    | Purpose                              |
| --------- | ------------------------------------ |
| Accuracy  | Overall classification correctness   |
| Precision | Quality of positive predictions      |
| Recall    | Ability to identify positive cases   |
| F1 Score  | Balance between precision and recall |
| ROC-AUC   | Ranking/discrimination capability    |

> **Important:** Actual values should be populated from the trained model rather than manually estimated.

---

# 🚫 Data Leakage Prevention

A key machine-learning consideration is preventing future information from entering the prediction process.

The feature:

```text
days_to_conversion
```

is excluded from the prediction feature set.

Why?

Because this information may only become available **after conversion has occurred**.

Including it could result in:

```text
Future Information
       ↓
Training Data
       ↓
Artificially High Performance
       ↓
Poor Real-World Generalization
```

Therefore, the feature is intentionally excluded.

---

# 📁 Batch Prediction

### Required CSV columns

```text
industry
service
lead_source
budget_inr
first_response_hours
followup_count
```

### Example

```csv
industry,service,lead_source,budget_inr,first_response_hours,followup_count
Technology,AI Development,Website,150000,2,3
Healthcare,Analytics,Referral,250000,1,5
Retail,Software,Social Media,80000,6,2
```

### Generated output

The application adds:

```text
conversion_probability
conversion_percentage
predicted_conversion
lead_priority
```

The output is automatically sorted from highest to lowest conversion probability.

---

# 📥 Output Example

```text
┌─────────────────────────────────────────────────────────┐
│                  PREDICTION OUTPUT                      │
├─────────────────────────────────────────────────────────┤
│ Lead       Probability       Prediction       Priority │
├─────────────────────────────────────────────────────────┤
│ Lead 001      91.4%          Convert           HIGH 🔥 │
│ Lead 002      74.8%          Convert           MEDIUM  │
│ Lead 003      42.1%          No Convert         LOW    │
└─────────────────────────────────────────────────────────┘
```

Results can be downloaded directly as a CSV file.

---

# ☁️ Deployment

The application is suitable for deployment on Streamlit-compatible cloud infrastructure.

## Streamlit Community Cloud

Deployment flow:

```text
GitHub Repository
       ↓
Connect Repository
       ↓
Select app.py
       ↓
Install requirements.txt
       ↓
Deploy
       ↓
Live Streamlit Application
```

### Required repository files

```text
app.py
requirements.txt
models/lead_conversion_model.joblib
04_jzd_sales_data.csv
```

---

## Server Deployment

Install dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
streamlit run app.py --server.address 0.0.0.0
```

---

# 🔐 Security & Production Considerations

Before production deployment:

* Do not commit confidential customer data.
* Add authentication and authorization.
* Store secrets using environment variables.
* Validate uploaded files.
* Restrict access to prediction data.
* Protect model artifacts.
* Configure secure logging.
* Avoid exposing sensitive information in error messages.
* Add rate limiting if exposed through an API.

---

# ⚠️ Known Limitations

### 1. CSV-Based Storage

The current version uses CSV files rather than a production database.

### 2. Static Model

The model is trained separately and loaded from a Joblib artifact.

Automatic retraining is not currently implemented.

### 3. Limited Features

Only six primary features are currently used for prediction.

### 4. No REST API

The current implementation is Streamlit-based.

### 5. No Authentication

Users are not currently authenticated.

### 6. Limited Explainability

The application does not currently provide SHAP/LIME explanations.

### 7. Dataset Dependency

The application requires the configured dataset and model artifact to be available.

---

# 🚀 Future Improvements

## 🤖 Advanced ML

* XGBoost
* LightGBM
* Ensemble learning
* Hyperparameter optimization
* Cross-validation
* Probability calibration
* Automated model selection

---

## 🧠 Explainable AI

Integrate:

* SHAP
* LIME
* Feature importance
* Individual prediction explanations

Example:

```text
Why is this lead HIGH priority?

✓ High budget
✓ Fast response
✓ Strong lead source
✓ High engagement
```

---

## 🗄️ Database Integration

Move from CSV to:

```text
PostgreSQL
MySQL
MongoDB
```

This would enable scalable and centralized data management.

---

## 🔌 REST API

A future architecture could use:

```text
Frontend
    ↓
FastAPI
    ↓
ML Model
    ↓
Database
```

Example:

```text
POST /predict
```

---

## 📡 Model Monitoring

Add monitoring for:

* Data drift
* Prediction drift
* Model performance
* Feature distribution
* Conversion trends

---

## 🔄 Automated MLOps

Future pipeline:

```text
New Sales Data
       ↓
Data Validation
       ↓
Feature Engineering
       ↓
Model Training
       ↓
Model Evaluation
       ↓
Model Registry
       ↓
Deployment
       ↓
Monitoring
       ↓
Retraining
```

---

# 🗺️ Project Roadmap

```text
Phase 1 ──────────────────────────────── ✅
Core ML Model
Data Processing
Model Evaluation

Phase 2 ──────────────────────────────── ✅
Streamlit Dashboard
Individual Prediction
Batch Prediction
Sales Analytics

Phase 3 ──────────────────────────────── 🔄
Explainable AI
Advanced Analytics
Authentication

Phase 4 ──────────────────────────────── 🚀
REST API
Database Integration
Cloud Deployment
Model Monitoring

Phase 5 ──────────────────────────────── 🔮
Automated MLOps
Real-Time Lead Scoring
CRM Integration
Automated Retraining
```

---

# 💼 Business Impact

The system is designed to help organizations move from **manual lead handling** toward **data-driven sales prioritization**.

### Without AI

```text
100 Leads
   ↓
Manual Evaluation
   ↓
Equal Attention
   ↓
Time & Resource Waste
```

### With AI

```text
100 Leads
   ↓
ML Lead Scoring
   ↓
Probability Ranking
   ↓
Priority Classification
   ↓
Focused Sales Effort
```

### Expected benefits

* 🎯 Better lead prioritization
* ⏱️ Reduced manual analysis
* 📊 Data-driven decision making
* 💰 Better allocation of sales resources
* 🔥 Faster identification of high-potential leads
* 📈 Improved sales intelligence

> **Note:** Actual business impact depends on model quality, data quality, sales execution, and deployment environment.

---

# 🧪 Quality & Engineering Practices

The application includes several engineering practices beyond basic ML inference:

```text
✓ Modular functions
✓ Exception handling
✓ Structured logging
✓ Environment configuration
✓ Streamlit caching
✓ Input validation
✓ Model serialization
✓ Batch processing
✓ Downloadable outputs
✓ Data leakage awareness
```

---

# 📊 End-to-End Project Summary

```text
┌───────────────────────────────────────────────────┐
│              AI SALES INTELLIGENCE               │
├───────────────────────────────────────────────────┤
│                                                   │
│  📊 Historical Data                               │
│          ↓                                        │
│  🧹 Data Processing                               │
│          ↓                                        │
│  🧠 Machine Learning                              │
│          ↓                                        │
│  📈 Model Evaluation                              │
│          ↓                                        │
│  💾 Joblib Model                                  │
│          ↓                                        │
│  🎯 Streamlit Application                         │
│          ↓                                        │
│  ┌────────────┬────────────┬──────────────┐      │
│  │ Dashboard  │ Prediction  │  Analytics   │      │
│  └────────────┴────────────┴──────────────┘      │
│          ↓                                        │
│  📁 Batch Prediction                              │
│          ↓                                        │
│  🔥 Lead Prioritization                           │
│          ↓                                        │
│  💡 Sales Recommendations                         │
│          ↓                                        │
│  📈 Data-Driven Decisions                         │
│                                                   │
└───────────────────────────────────────────────────┘
```

---

# 👨‍💻 Author

## Hadi Inamdar

**BE — Artificial Intelligence & Data Science**

### Areas of Interest

```text
Artificial Intelligence
Machine Learning
Data Science
Generative AI
Python Development
AI-Powered Applications
```

---

# 🏢 Project Context

| Attribute         | Details                                     |
| ----------------- | ------------------------------------------- |
| Project           | AI Sales Lead Prediction & Analytics System |
| Organization      | JZD Technologies                            |
| Category          | AI / Machine Learning                       |
| Application       | Sales Intelligence                          |
| Framework         | Streamlit                                   |
| Language          | Python                                      |
| Model Persistence | Joblib                                      |
| Visualization     | Plotly                                      |

---

# ⭐ Support

If you find this project useful or interesting, consider giving the repository a ⭐.

It helps support continued development and improvement.

---

# 📜 Disclaimer

This system is intended as a **decision-support tool**.

Machine-learning predictions are estimates based on historical data and should not be treated as guaranteed outcomes.

Final sales decisions should consider additional business context, customer interactions, and professional judgment.

---

<p align="center">

### 🎯 Predict Smarter. Prioritize Better. Sell Better.

**Built with 🐍 Python • 🤖 Machine Learning • 📊 Streamlit • 📈 Plotly**

</p>
