# Customer_Churn_Prediction
Project Overview
Customer churn is one of the most critical challenges faced by subscription-based businesses such as telecommunications, banking, insurance, and SaaS companies. Retaining existing customers is often more cost-effective than acquiring new ones.
This project aims to analyze customer behavior and predict whether a customer is likely to churn using Machine Learning techniques. A predictive model was developed using customer demographic information, service details, contract information, and payment preferences. The trained model is integrated into an interactive Streamlit dashboard that allows users to input customer information and receive real-time churn predictions.

Business Problem
Customer churn directly impacts company revenue and growth. Identifying customers who are likely to leave enables organizations to take proactive measures such as:
Personalized retention campaigns
Customer support interventions
Loyalty rewards and discounts
Service improvements
The objective of this project is to build a machine learning solution capable of predicting customer churn and supporting data-driven customer retention strategies.
Dataset
Dataset: Telco Customer Churn Dataset
The dataset contains customer information including:

Demographic details
Subscription services
Contract information
Payment methods
Customer tenure
Churn status
Selected Features
The model was trained using the following features:
Gender
Tenure
Contract Type
Payment Method
Internet Service
Tech Support
Target Variable
Churn (Yes / No)
Project Workflow
1. Data Collection
Imported customer churn dataset
Loaded and inspected data using Pandas
2. Data Cleaning
Handled missing values
Checked for duplicate records
Corrected data types where necessary
3. Exploratory Data Analysis (EDA)
Performed visual analysis using:
Matplotlib
Seaborn
Key analyses included:
Churn distribution
Contract type vs churn
Internet service vs churn
Payment method vs churn
Tech support vs churn
Customer tenure analysis
4. Data Preprocessing
One-Hot Encoding for categorical variables
Feature scaling using StandardScaler
Train-Test Split
5. Machine Learning Models
Multiple classification models were evaluated:
Logistic Regression
Decision Tree Classifier
Random Forest Classifier
6. Model Selection
Random Forest Classifier achieved the best performance and was selected as the final model.
7. Model Deployment
Developed an interactive Streamlit dashboard for real-time churn prediction.
Technologies Used
Programming Language
Python
Data Analysis
NumPy
Pandas
Data Visualization
Matplotlib
Seaborn
Machine Learning
Scikit-Learn
Save Model
Joblib
Deployment
Streamlit

Streamlit Dashboard Features:
User-friendly interface
Customer information input form
Real-time churn prediction
Machine learning model integration
Business-oriented decision support

Author
Tarakaa Shree A
Data Science Student | Machine Learning Enthusiast

Focused on building data-driven solutions using Python, Machine Learning, and Interactive Data Applications.





