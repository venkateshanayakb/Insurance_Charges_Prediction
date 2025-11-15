<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>Insurance Charges Prediction</title>
  <style>
    :root{
      --bg:#0b1220;
      --card:#0f1724;
      --muted:#94a3b8;
      --accent:#06b6d4;
      --glass: rgba(255,255,255,0.03);
      --glass-2: rgba(255,255,255,0.02);
      --white:#ecfeff;
      font-family: Inter, ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial;
    }
    html,body{height:100%;}
    body{
      margin:0;
      padding:32px;
      background: linear-gradient(180deg,#031124 0%, #071427 100%);
      color:var(--white);
      -webkit-font-smoothing:antialiased;
      -moz-osx-font-smoothing:grayscale;
    }
    .wrapper{
      max-width:980px;
      margin:0 auto;
    }
    header{
      display:flex;
      gap:20px;
      align-items:center;
      margin-bottom:18px;
    }
    .logo{
      width:86px;
      height:86px;
      border-radius:12px;
      background:linear-gradient(135deg,var(--accent),#1e7fd9);
      display:flex;
      align-items:center;
      justify-content:center;
      font-weight:700;
      font-size:24px;
      color:#042027;
      box-shadow: 0 8px 30px rgba(3,12,20,0.6);
    }
    h1{margin:0;font-size:20px;letter-spacing:0.2px;}
    p.lead{margin:6px 0 0;color:var(--muted);font-size:14px;}
    .badges{margin-left:auto;display:flex;gap:8px;flex-wrap:wrap;}
    .card{
      background:linear-gradient(180deg,var(--card), rgba(15,23,36,0.92));
      border-radius:12px;
      padding:20px;
      box-shadow: 0 12px 30px rgba(2,6,23,0.6);
      margin-top:18px;
    }
    .grid{
      display:grid;
      grid-template-columns: 1fr 320px;
      gap:18px;
      align-items:start;
    }
    .section{margin-bottom:18px;}
    h2{font-size:16px;margin:0 0 10px;}
    .muted{color:var(--muted);font-size:13px;line-height:1.5}
    .cta{
      display:inline-block;
      text-decoration:none;
      background:var(--accent);
      color:#022026;
      padding:10px 14px;
      border-radius:10px;
      font-weight:600;
      box-shadow: 0 8px 20px rgba(6,182,212,0.12);
    }
    .code{
      background:var(--glass);
      padding:12px;
      border-radius:8px;
      font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, "Roboto Mono", monospace;
      color: #d7f6fb;
      font-size:13px;
      overflow:auto;
    }
    table{
      width:100%;
      border-collapse:collapse;
      margin-top:8px;
      font-size:14px;
    }
    th,td{
      text-align:left;
      padding:10px 12px;
      border-bottom:1px solid rgba(255,255,255,0.03);
    }
    th{color:var(--muted);font-weight:600;font-size:13px}
    .right{
      background:var(--glass-2);
      border-radius:8px;
      padding:12px;
      color:var(--muted);
    }
    footer{margin-top:18px;color:var(--muted);font-size:13px;text-align:center}
    .meta-row{display:flex;gap:12px;flex-wrap:wrap;margin-top:8px}
    .pill{background:rgba(255,255,255,0.03);padding:8px 10px;border-radius:8px;font-size:13px;color:var(--muted)}
    .sample{display:flex;gap:8px;flex-direction:column}
    @media(max-width:900px){
      .grid{grid-template-columns:1fr; }
      .badges{justify-content:flex-end}
    }
  </style>
</head>
<body>
  <div class="wrapper">
    <header>
      <div class="logo">IC</div>
      <div>
        <h1>Insurance Charges Prediction</h1>
        <p class="lead">Streamlit app for quick estimation of individual health insurance charges using linear regression and min max scaling</p>
      </div>
      <div class="badges">
        <a href="https://insurancechargesprediction-wmhqgjcwk6mzpwpj7hltnx.streamlit.app/" target="_blank" title="Open live app">
          <img src="https://static.streamlit.io/badges/streamlit_badge_black_white.svg" alt="Streamlit app" style="height:28px;border-radius:6px">
        </a>
        <img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="python" style="height:20px;border-radius:6px">
        <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="license" style="height:20px;border-radius:6px">
        <img src="https://img.shields.io/badge/Status-Live-brightgreen.svg" alt="status" style="height:20px;border-radius:6px">
      </div>
    </header>

    <div class="grid">
      <main>
        <div class="card section">
          <h2>Quick start</h2>
          <p class="muted">Run locally in three steps on your machine</p>

          <div style="margin-top:12px" class="code">
            <pre style="margin:0">
git clone https://github.com/venky23/Insurance_Charges_Prediction.git
cd Insurance_Charges_Prediction
pip install -r requirements.txt
streamlit run app.py
            </pre>
          </div>
        </div>

        <div class="card section">
          <h2>What the app does</h2>
          <p class="muted">The app accepts basic personal and health attributes and returns an estimated insurance charge. It uses feature scaling and a trained linear regression model. It is designed for learning and demo use.</p>

          <h2 style="margin-top:14px">Prediction pipeline</h2>
          <table>
            <thead>
              <tr><th>Step</th><th>Description</th></tr>
            </thead>
            <tbody>
              <tr><td>Input capture</td><td>User fields age, sex, bmi, children, smoker, region</td></tr>
              <tr><td>Preprocessing</td><td>Min max scaling for numeric fields and encoding for categorical fields</td></tr>
              <tr><td>Model</td><td>Linear regression loaded from file and used for inference</td></tr>
              <tr><td>Output</td><td>Estimated insurance charge shown in app UI</td></tr>
            </tbody>
          </table>
        </div>

        <div class="card section">
          <h2>Usage examples</h2>
          <div class="sample">
            <div class="pill">Example 1 age 25, bmi 22.4, smoker no, children 0</div>
            <div class="pill">Example 2 age 40, bmi 28.5, smoker yes, children 2</div>
            <div class="pill">Example 3 age 55, bmi 31.6, smoker no, children 1</div>
          </div>

          <h2 style="margin-top:12px">Sample predictions</h2>
          <table>
            <thead><tr><th>Age</th><th>BMI</th><th>Smoker</th><th>Predicted charge</th></tr></thead>
            <tbody>
              <tr><td>25</td><td>22.4</td><td>No</td><td>8500</td></tr>
              <tr><td>40</td><td>28.5</td><td>Yes</td><td>22000</td></tr>
              <tr><td>55</td><td>31.6</td><td>No</td><td>16700</td></tr>
            </tbody>
          </table>
        </div>

        <div class="card section">
          <h2>Notes on reproducibility</h2>
          <p class="muted">Keep the model file and min max values in the repository root. Use the same scikit learn version used for training to avoid deserialization issues.</p>

          <div style="margin-top:12px" class="code">
            <pre style="margin:0">
# top of app.py
import joblib
import json
model = joblib.load("linear_regression_model.pkl")
with open("min_max_values.json") as f:
    minmax = json.load(f)
            </pre>
          </div>
        </div>
      </main>

      <aside class="right">
        <h2>Project summary</h2>
        <p class="muted">Streamlit app for fast insurance charge estimation. Good for teaching, prototyping and small demos. Deployed on Streamlit Cloud with a stable public link.</p>

        <div class="meta-row" style="margin-top:12px">
          <div class="pill">Model Linear Regression</div>
          <div class="pill">Framework Streamlit</div>
          <div class="pill">Language Python</div>
        </div>

        <h2 style="margin-top:14px">Files</h2>
        <table>
          <thead><tr><th>Name</th><th>Purpose</th></tr></thead>
          <tbody>
            <tr><td>app.py</td><td>Main Streamlit app</td></tr>
            <tr><td>linear_regression_model.pkl</td><td>Trained model</td></tr>
            <tr><td>min_max_values.json</td><td>Scaling values</td></tr>
            <tr><td>requirements.txt</td><td>Dependencies</td></tr>
          </tbody>
        </table>

        <h2 style="margin-top:14px">Live demo</h2>
        <p class="muted">Open the app in a new tab using the link below</p>
        <p style="margin-top:6px">
          <a class="cta" href="https://insurancechargesprediction-wmhqgjcwk6mzpwpj7hltnx.streamlit.app/" target="_blank">Open live app</a>
        </p>

        <h2 style="margin-top:14px">Deploy notes</h2>
        <ol style="color:var(--muted); padding-left:18px; margin-top:6px">
          <li>Push all files to GitHub repo root</li>
          <li>Create new app on Streamlit Cloud and connect to this repo</li>
          <li>Set main file to app.py and deploy</li>
        </ol>
      </aside>
    </div>

    <footer>
      <div style="margin-bottom:6px">Created by Mr. Nayak</div>
      <div>License MIT</div>
    </footer>
  </div>
</body>
</html>
