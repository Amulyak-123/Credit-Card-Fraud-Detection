# Credit-Card-Fraud-Detection
# 🚀 Credit Card Fraud Detection
🔍 A machine learning model to detect fraudulent credit card transactions.

## 📌 Project Overview
- Uses **XGBoost & SMOTETomek** to improve fraud detection accuracy.
- Handles **severe class imbalance (fraud cases < 0.2%)**.
- Deployed as an **API using FastAPI**.

---

## 📌 Dataset
- 📂 **Source:** [Kaggle Credit Card Fraud Dataset](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)
- **Features:**
  - `Time`: Seconds since first transaction
  - `Amount`: Transaction amount (scaled)
  - `V1-V28`: PCA-transformed features
  - `Class`: (0 = Non-Fraud, 1 = Fraud)

---

## 📌 Installation & Setup
### 🔹 **1️⃣ Clone the repository**
```sh
git clone https://github.com/your-username/credit-card-fraud-detection.git
cd credit-card-fraud-detection

 🔹 2️⃣ Create & Activate Virtual Environment (venv)
python -m venv venv  
venv\Scripts\activate(Activate on Windows)
source venv/bin/activate(Activate on Mac/Linux)

🔹 3️⃣ Install Dependencies
pip install -r requirements.txt

🔹 4️⃣ Preprocess the Dataset
python src/preprocess.py

🔹 5️⃣ Train the Model
python src/train_model.py

Install FastAPI & Uvicorn
pip install fastapi uvicorn pandas joblib pydantic

predict.py (FastAPI for Fraud Detection)

Run FastAPI Server
uvicorn src.predict:app --host 0.0.0.0 --port 8000 --reload
 Expected Output:INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)

Test API in Swagger UI (/docs)
1️⃣ Open http://127.0.0.1:8000/docs in your browser
2️⃣ Find the POST /predict endpoint
3️⃣ Click "Try it out" → Enter a test transaction
4️⃣ Click "Execute"

✅ Example Response:
{"fraud": true}

5️⃣ Test API with cURL (Command Line)
Run this command in the terminal:

sh
Copy
Edit
curl -X 'POST' 'http://127.0.0.1:8000/predict' -H 'Content-Type: application/json' -d '{
  "Amount_Scaled": 3.5,
  "Transaction_Hour": 22,
  "Transaction_Day": 5,
  "V1": -2.5, "V2": 3.2, "V3": -4.1, "V4": 6.3, "V5": -5.0,
  "V6": 2.8, "V7": -3.7, "V8": 1.9, "V9": -2.2, "V10": 4.1,
  "V11": -3.5, "V12": 5.6, "V13": -1.2, "V14": 2.9, "V15": -3.8,
  "V16": 4.7, "V17": -2.6, "V18": 3.5, "V19": -1.9, "V20": 2.4,
  "V21": -3.1, "V22": 4.2, "V23": -2.5, "V24": 5.1, "V25": -3.3,
  "V26": 2.7, "V27": -4.1, "V28": 3.9
}'
✅ Example Response:
{"fraud": true}


Test API in Python (requests Library){The file is alredy created as Test_api.py run this and test it the detection will be printed}
 Deploy FastAPI Using Uvicorn
gunicorn -w 4 -k uvicorn.workers.UvicornWorker src.predict:app


8️⃣ Common Issues & Fixes
Issue:	Solution
"Cannot reach page"	Ensure FastAPI is running: uvicorn src.predict:app --reload
Port 8000 blocked	Run in PowerShell (Admin): New-NetFirewallRule -DisplayName "Allow FastAPI" -Direction Inbound -LocalPort 8000 -Protocol TCP -Action Allow
FastAPI crashes on start	Ensure predict.py is correct & reinstall FastAPI: pip install fastapi uvicorn

Final Summary
step:Command
Run FastAPI	uvicorn src.predict:app --reload
Test in Swagger UI	Open http://127.0.0.1:8000/docs
Test via cURL	Run curl -X 'POST' ...
Deploy with Gunicorn	gunicorn -w 4 -k uvicorn.workers.UvicornWorker src.predict:app

Model Performance
Metric	Score
ROC-AUC	0.91
Precision	85%
Recall	90%

"# Credit-Card-Fraud-Detection" 
"# Credit-Card-Fraud-Detection" 
