import joblib
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, classification_report

# ✅ Load data & model
df = pd.read_csv("Data/processed_data.csv")
model = joblib.load("models/fraud_detection.pkl")

# ✅ Ensure features match training
X = df.drop(columns=['Class'])
y = df['Class']

# ✅ Keep only features the model was trained on
X = X[model.feature_names_in_]

# ✅ Predict
y_pred = model.predict(X)

# ✅ Confusion Matrix
cm = confusion_matrix(y, y_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.savefig("results/confusion_matrix.png")
plt.show()

# ✅ Print classification report
print(classification_report(y, y_pred))
