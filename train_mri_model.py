import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib

# Load dataset
df = pd.read_csv('oasis_longitudinal.csv', sep='\t')  # <-- Add sep='\t' for TSV

# Preprocess the data
# Encode categorical variables
df['M/F'] = df['M/F'].map({'M': 1, 'F': 0})
df['Group'] = df['Group'].map({'Demented': 1, 'Converted': 1, 'Nondemented': 0})

# Handle missing values
df['SES'] = df['SES'].fillna(df['SES'].median())
df = df.dropna(subset=['MMSE', 'CDR'])

# Drop irrelevant columns
df = df.drop(['Subject ID', 'MRI ID', 'Visit', 'MR Delay', 'Hand'], axis=1)

# Features and target
features = ['Age', 'M/F', 'EDUC', 'SES', 'MMSE', 'CDR', 'eTIV', 'nWBV', 'ASF']
X = df[features]
y = df['Group']

# Get feature limits
limits = X.agg(['min', 'max']).T.to_dict(orient='index')

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)
print("Classification Report:\n", classification_report(y_test, y_pred))

# Save the model (optional, for integration)
joblib.dump(model, 'mri_model.pkl')
joblib.dump(limits, 'mri_limits.pkl')

# Input with validation (for testing)
print("\n--- Alzheimer’s MRI Risk Predictor ---")
user_input = {}
for feature in features:
    fmin = limits[feature]['min']
    fmax = limits[feature]['max']
    while True:
        try:
            if feature == 'M/F':
                value = input(f"Enter {feature} (1 for Male, 0 for Female): ")
                value = float(value)
                if value in [0, 1]:
                    user_input[feature] = value
                    break
                else:
                    print(f"⚠️ Please enter 0 or 1")
            else:
                value = float(input(f"Enter {feature} (range: {fmin} to {fmax}): "))
                if fmin <= value <= fmax:
                    user_input[feature] = value
                    break
                else:
                    print(f"⚠️ Please enter a value within {fmin} and {fmax}")
        except ValueError:
            print("❌ Invalid input. Please enter a number.")

# Convert input to DataFrame
input_df = pd.DataFrame([user_input])

# Predict
prediction = model.predict(input_df)[0]
if prediction == 1:
    print("\n🧠 The model predicts a HIGH RISK of Alzheimer’s.")
else:
    print("\n✅ The model predicts a LOW RISK of Alzheimer’s.")