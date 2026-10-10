# Credit Card Approval Analysis and Prediction Using Machine Learning

## Project Overview
This project analyzes applicant information and uses Machine Learning algorithms to predict credit card approval status. A Streamlit web application allows users to enter applicant details and view model predictions.

## Objectives
- Analyze applicant and financial data.
- Perform data cleaning and preprocessing.
- Train and compare multiple Machine Learning models.
- Evaluate model performance using standard metrics.
- Build an interactive prediction application using Streamlit.

## Technologies Used
- Python
- Pandas, NumPy
- Matplotlib, Seaborn
- Scikit-learn
- Streamlit
- Joblib
- Jupyter Notebook

## Machine Learning Models
- Logistic Regression
- Decision Tree
- K-Nearest Neighbors (KNN)
- Random Forest
- Gradient Boosting
- Support Vector Machine (SVM)
- Gaussian Naive Bayes

## Workflow
1. Data Collection
2. Data Understanding and Cleaning
3. Exploratory Data Analysis (EDA)
4. Data Preprocessing
5. Train-Test Split
6. Model Training
7. Model Evaluation and Comparison
8. Best Model Selection
9. Model Saving
10. Streamlit Application Development

## Model Evaluation
The models are evaluated using:

- Accuracy
- Precision
- Recall
- F1-Score
  
## Model Accuracy

The Decision Tree classifier achieved the highest accuracy of **99.92%**, with a precision of **99.96%**, recall of **99.96%**, and F1-score of **99.96%** among the evaluated models.

The Decision Tree was selected as the best-performing model based on the evaluation results. Since the dataset contains a highly imbalanced target variable, further validation using a confusion matrix, class-specific metrics, and data leakage checks is recommended.

## Streamlit Application
The application accepts applicant details and displays the predicted credit card approval status.

To run the application:

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Project Structure

```text
Credit-Card-Approval-Prediction/
├── Application_Data.csv
├── Credit_Card_Approval_Analysis.ipynb
├── Credit_Card_Approval_Model.pkl
├── app.py
├── requirements.txt
└── README.md
```

## Conclusion
This project demonstrates an end-to-end Machine Learning workflow, from data analysis and model evaluation to deployment through a Streamlit web application.

## Author
**G. Praveena**  
Data Science

