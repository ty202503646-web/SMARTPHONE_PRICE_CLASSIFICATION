# 📱 Smartphone Price Classification System using Machine Learning and Django

## Project Description

The Smartphone Price Classification System is a web-based machine learning application developed using Python, Django Framework, and Scikit-learn. The system predicts the price category of a smartphone based on its specifications such as RAM, battery power, screen resolution, internal memory, and other hardware features.

The application allows users to enter smartphone specifications through a web interface and automatically predicts the corresponding price range using a trained Machine Learning model.

---

# Project Objectives

The main objectives of this project are:

- Develop a Machine Learning model capable of classifying smartphone prices.
- Perform data cleaning and preprocessing techniques before training.
- Compare different machine learning algorithms.
- Deploy the best-performing model using Django.
- Provide a user-friendly web application for smartphone price prediction.

---

# Dataset

**Dataset Name**

Mobile Price Classification Dataset

**Source**

https://www.kaggle.com/datasets/iabhishekofficial/mobile-price-classification

The dataset contains **2,000 smartphone records** with **20 input features** and **1 target variable**.

---

# Dataset Features

| Feature | Description |
|----------|-------------|
| battery_power | Battery capacity (mAh) |
| blue | Bluetooth availability (0 = No, 1 = Yes) |
| clock_speed | Processor clock speed (GHz) |
| dual_sim | Dual SIM support |
| fc | Front camera megapixels |
| four_g | 4G support |
| int_memory | Internal memory (GB) |
| m_dep | Mobile depth (cm) |
| mobile_wt | Mobile weight (grams) |
| n_cores | Number of processor cores |
| pc | Primary camera megapixels |
| px_height | Pixel resolution height |
| px_width | Pixel resolution width |
| ram | RAM capacity (MB) |
| sc_h | Screen height |
| sc_w | Screen width |
| talk_time | Battery talk time (hours) |
| three_g | 3G support |
| touch_screen | Touchscreen support |
| wifi | WiFi support |
| price_range | Smartphone price category (Target Variable) |

---

# Data Cleaning and Preparation

The following preprocessing techniques were applied:

- Checked missing values
- Removed duplicate records
- Verified data consistency
- Checked data types
- Feature and target separation
- Train-Test Split (80%-20%)

No missing values were found in the dataset.

---

# Feature Engineering

The following feature engineering techniques were applied:

- Feature Selection
- Removal of unnecessary attributes
- Preparation of predictor variables (X)
- Preparation of target variable (y)

---

# Machine Learning Algorithm

Current implemented model:

- Random Forest Classifier

Libraries used:

- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Joblib

---

# Model Performance

Accuracy

```
89.25%
```

Classification Report

```
Precision : 0.89
Recall    : 0.89
F1 Score  : 0.89
```

Confusion Matrix

```
[[101   4   0   0]
 [  5  79   7   0]
 [  0   6  80   6]
 [  0   0  15  97]]
```

---

# Django Web Application Features

The deployed web application includes:

- Home Page
- Prediction Form
- Prediction Result
- Prediction History
- Dashboard
- About Page
- Dataset Information Page

---

# Technologies Used

- Python 3.11
- Django 5
- Scikit-learn
- Pandas
- NumPy
- Matplotlib
- HTML
- CSS
- SQLite3
- Git
- GitHub

---

# Installation Guide

Clone the repository

```bash
git clone https://github.com/ty202503646-web/SMARTPHONE_PRICE_CLASSIFICATION.git
```

Navigate to the project

```bash
cd SMARTPHONE_PRICE_CLASSIFICATION
```

Create virtual environment

```bash
python -m venv venv
```

Activate virtual environment

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Apply migrations

```bash
python manage.py migrate
```

Run the server

```bash
python manage.py runserver
```

Open

```
http://127.0.0.1:8000/
```

---

# Developer

Angelica Ignacio

Bachelor of Science in Computer Science

Western Mindanao State University

---

# License

This project is developed for academic purposes as part of the Machine Learning Final Project.# SMARTPHONE_PRICE_CLASSIFICATION
Machine Learning Smartphone Price Classification System using Django Framework
