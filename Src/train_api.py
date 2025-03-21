import requests

# ✅ API URL
url = "http://127.0.0.1:8000/predict"

# ✅ Example Transaction Data
transaction_data = {
  "Amount_Scaled": 5.0,
  "Transaction_Hour": 3,
  "Transaction_Day": 6,
  "V1": -10.5,
  "V2": 8.3,
  "V3": -5.1,
  "V4": 12.0,
  "V5": -8.5,
  "V6": 10.7,
  "V7": -6.9,
  "V8": 9.3,
  "V9": -7.1,
  "V10": 11.2,
  "V11": -12.4,
  "V12": 14.5,
  "V13": -9.8,
  "V14": 7.6,
  "V15": -10.4,
  "V16": 9.2,
  "V17": -11.3,
  "V18": 12.8,
  "V19": -9.5,
  "V20": 15.0,
  "V21": -10.2,
  "V22": 8.7,
  "V23": -13.1,
  "V24": 11.5,
  "V25": -8.9,
  "V26": 9.8,
  "V27": -7.3,
  "V28": 10.0
}


# ✅ Send POST Request
response = requests.post(url, json=transaction_data)

# ✅ Print Response
print("Response:", response.json())
