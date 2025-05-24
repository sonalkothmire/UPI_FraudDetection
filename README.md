# UPI Fraud Detection

This project implements a Fraud Detection Model designed to identify fraudulent financial transactions using machine learning. The model leverages a  Gradient Boosting model to classify transactions as either fraudulent or non-fraudulent based on several transaction-related features. By utilizing data from accounts' balance changes and transaction amounts, the model efficiently detects suspicious activities.

# Project Overview

The primary objective of this project is to detect fraudulent transactions in financial systems. The model is trained on a dataset containing several features like transaction amount, account balances before and after the transaction, and account information. By leveraging Gradient Boosting, the model can differentiate between legitimate and fraudulent transactions.

# Model Approach

## 1. Data Preprocessing:
The dataset is cleaned and transformed for model training by handling missing values, feature scaling, and encoding categorical variables.

## 2. Feature Engineering:
Derived features—such as the difference in account balances—play a crucial role in detecting discrepancies that indicate fraud.

## 3. Modeling:
A Gradient Boosting model is used, and hyperparameter tuning optimizes its performance.

## 4.Evaluation:
The model’s effectiveness is measured via precision, recall, F1-score, and other metrics.

 # Features
## Key features used for training the model include:

1.step: Time step of the transaction.

2.type: Type of transaction (e.g., CASH-IN, CASH-OUT).

3.amount: Transaction amount.

4.nameOrig: Origin account name.

5.oldbalanceOrg: Original balance of the origin account.

6.newbalanceOrig: New balance of the origin account.

7.nameDest: Destination account name.

8.oldbalanceDest: Original balance of the destination account.

9.newbalanceDest: New balance of the destination account.

# Model Training & Hyperparameter Tuning

## Hyperparameter Tuning :
Grid search was used to optimize the Gradient Boosting Classifier. The best parameters found are:

{'learning_rate':0.1, 'n_estimatores':200}

## Best F1-Score : 
The tuned model achieved an F1-score of 0.9967, demonstrating its accuracy in classifying transactions.

# Model Performance

## Evaluation Metrics

The model’s performance metrics include:

F1-Score: 0.9762
Precision: 0.02
Recall: 0.97

| Class | Precision | Recall | F1-Score | Support |
|-|-|-|-|-|
|0.0(Non-Fraud)|1.00|0.98|0.99|999120|
|1.0(Fraud)|0.02|0.97|0.07|880|
|Accuracy| | | 0.96|1000000| 
|Macro avg|0.51|0.97|0.51|1000000|
|Weighted Avg|1.00|0.96|0.98|1000000|
