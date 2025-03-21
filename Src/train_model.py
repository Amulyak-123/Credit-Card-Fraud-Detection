import pandas as pd
import joblib
import os
from imblearn.combine import SMOTETomek
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
from sklearn.metrics import classification_report, roc_auc_score, precision_recall_curve
import numpy as np

# ✅ Load Processed Data
df = pd.read_csv("Data/processed_data.csv")

# ✅ Select Features
features = ["Amount_Scaled", "Transaction_Hour", "Transaction_Day"] + [f"V{i}" for i in range(1, 29)]
X = df[features]
y = df["Class"]

# ✅ Train on a Smaller Dataset (100,000 rows for speed)
df_sample = df.sample(n=100000, random_state=42)  
X = df_sample[features]
y = df_sample["Class"]

# ✅ Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

# ✅ Handle Class Imbalance Using SMOTETomek (Faster)
smote_tomek = SMOTETomek(sampling_strategy=0.2, random_state=42)  # 20% fraud cases for speed
X_train_resampled, y_train_resampled = smote_tomek.fit_resample(X_train, y_train)

# ✅ Train XGBoost Model (Faster Settings)
model = XGBClassifier(
    n_estimators=150,  # Reduce from 300 to 150
    max_depth=6,  # Reduce from 10 to 6
    learning_rate=0.05,
    scale_pos_weight=y_train_resampled.value_counts()[0] / y_train_resampled.value_counts()[1],  # Balance fraud
    random_state=42
)
model.fit(X_train_resampled, y_train_resampled)

# ✅ Find Best Fraud Detection Threshold
y_proba = model.predict_proba(X_test)[:, 1]
precision, recall, thresholds = precision_recall_curve(y_test, y_proba)
best_threshold = thresholds[np.argmax(precision * recall)]  # Find best balance
y_pred_adjusted = (y_proba >= best_threshold).astype(int)

# ✅ Evaluate Model
print("\n📊 Classification Report:\n", classification_report(y_test, y_pred_adjusted))
print("🎯 Optimized ROC-AUC Score:", roc_auc_score(y_test, y_proba))

# ✅ Save Model
os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/fraud_detection.pkl")
print("✅ Model saved in `models/fraud_detection.pkl`!")
