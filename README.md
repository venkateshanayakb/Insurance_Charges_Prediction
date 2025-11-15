<div align="center">
<strong>🏥 INSURANCE CHARGES PREDICTION</strong>

An elegant Machine Learning application that predicts medical insurance charges using a Linear Regression model wrapped in a clean Streamlit interface.

<br> <img src="https://static.streamlit.io/badges/streamlit_badge_black_white.svg"> <img src="https://img.shields.io/badge/Python-3.10+-blue?style=flat-square"> <img src="https://img.shields.io/badge/Framework-Streamlit-red?style=flat-square"> <img src="https://img.shields.io/badge/Model-Linear%20Regression-orange?style=flat-square"> <img src="https://img.shields.io/badge/Status-Live-brightgreen?style=flat-square"> <img src="https://img.shields.io/badge/License-MIT-green?style=flat-square">

<br><br>

🔗 Live App:

https://insurancechargesprediction-wmhqgjcwk6mzpwpj7hltnx.streamlit.app/

</div>
1 Overview

This project estimates individual health insurance charges using demographic and lifestyle attributes.
It showcases a complete ML workflow including preprocessing, scaling and deployment in a user friendly Streamlit application.

This project suits healthcare analytics learners and beginners exploring ML deployment.

2 Features

• Interactive modern UI
• Real time predictions
• Built in min max scaling
• Lightweight linear regression model
• One click Streamlit Cloud deployment
• Easy to extend and modify

3 Workflow Diagram

Github renders this diagram cleanly.

flowchart TD
    A[User Inputs<br>Age, BMI, Gender, Smoker, Region] --> B[Preprocessing<br>Min Max Scaling]
    B --> C[Model<br>Linear Regression .pkl]
    C --> D[Prediction<br>Estimated Charges]
    D --> E[Streamlit UI<br>Result Display]

4 Input Features

| Feature  | Type     | Details               |
| -------- | -------- | --------------------- |
| Age      | Numeric  | Person’s age in years |
| BMI      | Numeric  | Body Mass Index       |
| Gender   | Category | Male or Female        |
| Smoker   | Category | Yes or No             |
| Region   | Category | NE, NW, SE, SW        |
| Children | Numeric  | Number of dependents  |

5 Project Structure
Insurance_Charges_Prediction/
│── app.py
│── linear_regression_model.pkl
│── min_max_values.json
│── requirements.txt
│── README.md

6 Installation

Install locally with Python

git clone https://github.com/venky23/Insurance_Charges_Prediction.git

cd Insurance_Charges_Prediction

pip install -r requirements.txt

streamlit run app.py

7 Usage

Enter user details in the interface
Tap “Predict”
View predicted insurance charges instantly.

8 Example Predictions

| Age | BMI  | Smoker | Predicted Charges |
| --- | ---- | ------ | ----------------- |
| 30  | 24.3 | No     | ₹8400             |
| 45  | 29.7 | Yes    | ₹23700            |
| 52  | 31.1 | No     | ₹16400            |

9 Deployment

Deployed on Streamlit Cloud.
Any push to the main branch automatically updates the live application.

10 Contributing

Fork the repository, create a new branch and submit a pull request for improvements or new features.

11 License

This project is released under the MIT License.
