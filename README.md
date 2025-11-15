Insurance Charges Prediction










A lightweight machine learning app built using Streamlit that predicts medical insurance charges based on user inputs such as age, gender, BMI, and smoking habits.
The model is powered by Linear Regression, combined with min-max scaling for accurate estimations.

🔗 Live Demo

▶ Launch the App
https://insurancechargesprediction-wmhqgjcwk6mzpwpj7hltnx.streamlit.app/

📌 Table of Contents

Overview

Features

How the Model Works

Tech Stack

Project Structure

Installation

Usage

Sample Predictions

Deployment

Contributing

License

📘 1 Overview

Medical insurance pricing varies based on personal attributes.
This project predicts expected insurance charges using a trained linear regression model on structured health-related features.

The tool is ideal for
• students learning ML deployment
• healthcare analytics beginners
• insurance modelling demonstrations
• regression modelling practice

⭐ 2 Features

✔ Clean and interactive Streamlit UI
✔ Real-time insurance charge predictions
✔ Min-max feature scaling
✔ Lightweight and easy to deploy
✔ Beginner-friendly project structure
✔ Fully open source and reproducible

🧠 3 How the Model Works

The prediction pipeline uses:

Step	Description
Data Preprocessing	Handles numerical and categorical conversion
Min-Max Scaling	Normalises age, bmi, children
Linear Regression Model	Trained on health insurance dataset
Inference on UI	Real-time prediction based on user inputs

The formula used is

ŷ = β0 + β1x1 + β2x2 + ... + βnxn

🛠 4 Tech Stack
Component	Technology
Language	Python
Web App	Streamlit
Model	Linear Regression (scikit-learn)
Data	Insurance Dataset
Deployment	Streamlit Cloud
📁 5 Project Structure
Insurance_Charges_Prediction/
│── app.py                  
│── linear_regression_model.pkl
│── min_max_values.json
│── requirements.txt
│── README.md

⚙️ 6 Installation (Run Locally)
Step 1: Clone the Repository
git clone https://github.com/venky23/Insurance_Charges_Prediction.git
cd Insurance_Charges_Prediction

Step 2: Install Dependencies
pip install -r requirements.txt

Step 3: Launch the App
streamlit run app.py

▶ 7 Usage

Once the app launches you can
• Select gender
• Choose region
• Toggle smoker status
• Input age, BMI, children count
and click Predict Charges.

The output shows the estimated insurance cost in Indian Rupees or USD equivalent depending on your extension.

📊 8 Sample Predictions
Age	BMI	Smoker	Predicted Charge
25	22.4	No	8 500 ₹
40	28.5	Yes	22 000 ₹
55	31.6	No	16 700 ₹

These numbers vary based on your model parameters.

☁️ 9 Deployment

This project is deployed on Streamlit Cloud, providing a stable URL for sharing.

You can redeploy by visiting
https://share.streamlit.io

and connecting your GitHub repo.

🤝 10 Contributing

Contributions are welcome.
Steps

1 Fork the repository
2 Create a new branch
3 Commit your changes
4 Open a pull request

📜 11 License

This project is licensed under the MIT License, allowing free reuse and modification.
