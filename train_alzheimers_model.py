import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# Load dataset
df = pd.read_csv('alzheimers_disease_data.csv')

# Drop irrelevant columns
df = df.drop(['PatientID', 'DoctorInCharge'], axis=1)

# Features and target
features = ['Age', 'Gender', 'Ethnicity', 'EducationLevel', 'BMI', 'Smoking', 
            'AlcoholConsumption', 'PhysicalActivity', 'DietQuality', 'SleepQuality',
            'FamilyHistoryAlzheimers', 'CardiovascularDisease', 'Diabetes', 'Depression',
            'HeadInjury', 'Hypertension', 'SystolicBP', 'DiastolicBP', 'CholesterolTotal',
            'CholesterolLDL', 'CholesterolHDL', 'CholesterolTriglycerides', 'MMSE',
            'FunctionalAssessment', 'MemoryComplaints', 'BehavioralProblems', 'ADL',
            'Confusion', 'Disorientation', 'PersonalityChanges', 'DifficultyCompletingTasks',
            'Forgetfulness']

# Features and target
X = df.drop('Diagnosis', axis=1)
y = df['Diagnosis']

# Get feature limits
limits = df.drop('Diagnosis', axis=1).agg(['min', 'max']).T.to_dict(orient='index')

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)
print("Classification Report:\n", classification_report(y_test, y_pred))

# Save model and limits
import joblib
joblib.dump(model, 'alzheimers_model.pkl')
joblib.dump(limits, 'alzheimers_limits.pkl')
print("\nModel and limits saved successfully!")
print(f"Feature limits saved for {len(features)} features")

print("\n" + "="*60)
print("ALZHEIMER'S RISK PREDICTION - ENTER PATIENT DATA")
print("="*60)

input_data = {}
for feature in features:
    while True:
        try:
            value = float(input(f"Enter {feature} ({limits[feature]['min']:.2f} - {limits[feature]['max']:.2f}): "))
            if limits[feature]['min'] <= value <= limits[feature]['max']:
                input_data[feature] = value
                break
            else:
                print(f"❌ Value out of range! Must be between {limits[feature]['min']:.2f} and {limits[feature]['max']:.2f}")
        except ValueError:
            print("❌ Invalid input! Please enter a number.")

input_df = pd.DataFrame([input_data])
prediction = model.predict(input_df)[0]

print("\n" + "="*60)
if prediction == 1:
    print("🧠 PREDICTION: HIGH RISK of Alzheimer's Disease")
else:
    print("✅ PREDICTION: LOW RISK of Alzheimer's Disease")
print("="*60)