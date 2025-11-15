🏥 Insurance Charges Prediction

Predict medical insurance charges using an elegantly designed ML + Streamlit application.

<div align="center"> <img src="https://img.freepik.com/free-vector/medical-insurance-concept-illustration_114360-2344.jpg" width="650"> </div>
<div align="center">










</div>
🔗 Live Demo

👉 Open App:
https://insurancechargesprediction-wmhqgjcwk6mzpwpj7hltnx.streamlit.app/

📘 Overview

This project predicts health insurance charges using demographic and lifestyle parameters.
It demonstrates a complete ML pipeline wrapped in a clean Streamlit UI:
data preprocessing
min-max scaling
linear regression model
interactive deployment.

This project is ideal for healthcare analytics learners, ML beginners, and portfolio building.

✨ Features

🟦 Intuitive Streamlit interface
🟩 Real-time ML-based prediction
🟨 Min-max feature scaling
🟧 Lightweight, fast linear regression model
🟪 Easy to deploy and extend
🟫 Full reproducibility with included files

🧠 How It Works
🔄 Workflow Diagram
        ┌────────────┐
        │   Dataset   │
        └──────┬──────┘
               │
               ▼
      ┌──────────────────┐
      │  Preprocessing    │
      │ Min-Max Scaling   │
      └────────┬─────────┘
               │
               ▼
     ┌──────────────────┐
     │ Linear Regression │
     └────────┬─────────┘
               │
               ▼
     ┌──────────────────┐
     │ Streamlit UI     │
     └──────────────────┘

📊 Model Inputs
Feature	Type	Description
Age	Numeric	Person’s age in years
BMI	Numeric	Body Mass Index
Gender	Category	Male, Female
Smoker	Category	Yes or No
Region	Category	NE, NW, SE, SW
Children	Numeric	Number of dependents
📁 Project Structure
Insurance_Charges_Prediction/
│── app.py
│── linear_regression_model.pkl
│── min_max_values.json
│── requirements.txt
│── README.md

⚙️ Installation
git clone https://github.com/venky23/Insurance_Charges_Prediction.git
cd Insurance_Charges_Prediction
pip install -r requirements.txt
streamlit run app.py


▶ Usage

Open the web app

Enter age, BMI, children

Select region, gender, smoker status

Click Predict Charges

View instant estimated charges

🌈 Sample Predictions
| Age | BMI  | Smoker | **Predicted Charges** |
| --- | ---- | ------ | --------------------- |
| 28  | 23.4 | ❌ No   | 🟩 **₹8 100**         |
| 42  | 29.8 | ✔ Yes  | 🟥 **₹22 400**        |
| 55  | 31.2 | ❌ No   | 🟨 **₹16 300**        |


☁ Deployment

The app is deployed on Streamlit Cloud.
Updating your GitHub repository automatically updates the live app.

🤝 Contributing

Pull requests and new ideas are welcome.
Raise an issue if you want a new feature or improvement.

📜 License

MIT License. Free to use, modify, and distribute.
