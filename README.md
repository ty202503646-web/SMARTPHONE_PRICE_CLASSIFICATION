Smartphone Price Range Classification Using Machine Learning

PROJECT DESCRIPTION

This project is a Machine Learning-based Smartphone Price Range Classification System developed using Python, Scikit-learn, and Django.

The system predicts the price range category of a smartphone based on its specifications instead of predicting its exact selling price.

The trained machine learning model is integrated into a Django web application where users can input smartphone specifications and instantly receive a predicted price range.

PROJECT OBJECTIVES

The objectives of this project are to:

-Develop a machine learning classification model for smartphone price range prediction.
-Compare the performance of five different machine learning algorithms.
-Perform data cleaning and feature engineering.
-Evaluate different versions of the dataset.
-Deploy the best-performing model into a Django web application.
-Dataset

DATASET NAME

Smartphone Price Prediction Dataset

SOURCE

https://www.kaggle.com/datasets/iabhishekofficial/mobile-price-classification

DATASET FEATURES

Feature	                                  Description

battery_power	                          Battery capacity (mAh)
blue	                                  Bluetooth support (0 = No, 1 = Yes)
clock_speed	Processor                     speed (GHz)
dual_sim	                              Dual SIM support
fc	                                      Front camera resolution (MP)
four_g	                                  4G support
int_memory	                              Internal storage (GB)
m_dep	                                  Mobile thickness
mobile_wt	                              Mobile weight (grams)
n_cores	                                  Number of processor cores
pc	                                      Primary camera resolution (MP)
px_height	                              Screen pixel height
px_width	                              Screen pixel width
ram	                                      RAM capacity (MB)
sc_h	                                  Screen height
sc_w	                                  Screen width
talk_time	                              Battery talk time (hours)
three_g	                                  3G support
touch_screen	                          Touch screen support
wifi	                                  WiFi support
price_range	                             Target class (0–3)



TARGET VARIABLE

price_range

Value	                                  Meaning
0	                                    Low-End Phone
1	                                    Budget Phone
2	                                    Mid-Range Phone
3	                                    Flagship Phone


DATA CLEANING AND PREPARATION

The following preprocessing techniques were performed:

-Checked and removed duplicate records
-Checked missing (NULL) values
-Verified data consistency
-Standardized numerical features using StandardScaler (Version 3)
-Created multiple dataset versions for experimentation


DATASET VERSIONS

Version 1
        - Raw dataset

Version 2
    Cleaned dataset
        - Duplicate checking
        - Missing value checking
        - Data consistency validation

Version 3
    Scaled dataset
        - StandardScaler applied
        - Used for Logistic Regression and SVM experiments


Machine Learning Algorithms Used
       - Random Forest Classifier
        - Decision Tree Classifier
        - K-Nearest Neighbors (KNN)
        - Logistic Regression
        - Support Vector Machine (SVM)

    
 Model Performance
    Model	              Version 1	                  Version 2	         Version 3

Random Forest	           89.25%	                   89.25%	           89.25%
Decision Tree	           83.25%	                   83.25%	           83.75%
KNN	                       94.25%	                   94.25%	           53.00%
Logistic Regression	       75.75%	                   75.75%	           97.75%
SVM	                       96.50%	                   96.50%	           89.25%

Best Model
    Algorithm: Logistic Regression

    Dataset Version: Version 3 (Scaled Dataset)
        - Accuracy: 97.75%

Evaluation Metrics:
        Accuracy
        Precision
        Recall
        F1-score
        Confusion Matrix


Django Web Application Features
    The deployed Django application includes:
        - Smartphone prediction form
        - Price range prediction
        - Prediction history
        - Dashboard
        - Prediction analytics chart
        - Update prediction
        - Delete prediction
        - Export prediction history to CSV


Technologies Used
    - Python
    - Pandas
    - NumPy
    - Scikit-learn
    - Matplotlib
    - Django
    - Bootstrap 5
    - SQLite3


Installation
    git clone <https://github.com/ty202503646-web/SMARTPHONE_PRICE_CLASSIFICATION>

cd SMARTPHONE_PRICE_CLASSIFICATION

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver
Author

Angelica Ignacio

Bachelor of Science in Computer Science

Western Mindanao State University