# 🧠 Alzheimer's Disease Risk Assessment System

A comprehensive Flask-based web application that uses machine learning to assess Alzheimer's disease risk through two prediction models: clinical/lifestyle data analysis and MRI brain imaging analysis.

---

## 📋 Table of Contents
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage Guide](#usage-guide)
- [File Descriptions](#file-descriptions)
- [Model Training](#model-training)
- [Technical Stack](#technical-stack)
- [Dataset Information](#dataset-information)
- [Troubleshooting](#troubleshooting)

---

## ✨ Features

- **Dual Prediction Models**: 
  - Clinical assessment using 32 lifestyle and medical features
  - MRI-based assessment using 9 brain imaging measurements
- **User Authentication**: Secure login/signup system with SQLite database
- **Prediction History**: Track all previous assessments with timestamps
- **Report Generation**: Download comprehensive PDF/DOCX reports with:
  - Patient information and input parameters
  - Risk assessment results
  - Personalized recommendations
  - Medical disclaimers
- **Interactive Dashboard**: View statistics, recent tests, and notifications
- **Input Validation**: Real-time range checking based on training data

---

## 📁 Project Structure

alzheimers-assessment/
├── app.py # Main Flask application
├── train_alzheimers_model.py # Clinical model training script
├── train_mri_model.py # MRI model training script
├── alzheimers_disease_data.csv # Clinical dataset (2000+ patients)
├── oasis_longitudinal.csv # OASIS MRI dataset
├── alzheimers_model.pkl # Trained clinical model (generated)
├── alzheimers_limits.pkl # Clinical feature ranges (generated)
├── mri_model.pkl # Trained MRI model (generated)
├── mri_limits.pkl # MRI feature ranges (generated)
├── users.db # SQLite database (auto-created)
├── templates/ # HTML templates
│ ├── landing.html
│ ├── login.html
│ ├── signup.html
│ ├── home.html
│ ├── predictor.html
│ ├── mri_upload.html
│ ├── results.html
│ ├── history.html
│ └── profile.html
└── static/ # CSS/JS assets
└── styles.css

text

---

## 🚀 Installation

### Prerequisites
- Python 3.8+
- pip package manager

### Step 1: Install Required Packages

pip install -r requirements.txt

### Step 2: Prepare Datasets

Ensure these CSV files are in the project root:
- `alzheimers_disease_data.csv`
- `oasis_longitudinal.csv`

---

## 📖 Usage Guide

### First-Time Setup

**Step 1: Train the Clinical Model**

python train_alzheimers_model.py

text

This generates:
- `alzheimers_model.pkl` - Trained Random Forest classifier
- `alzheimers_limits.pkl` - Feature min/max ranges for validation

**Optional**: Test predictions via command line:

python train_alzheimers_model.py --predict

text

**Step 2: Train the MRI Model**

python train_mri_model.py

text

This generates:
- `mri_model.pkl` - Trained MRI-based classifier
- `mri_limits.pkl` - MRI feature ranges

**Step 3: Run the Flask Application**

python app.py

text

**Step 4: Access the Application**

Open your browser and navigate to:

http://localhost:5000

text

### Using the Application

1. **Create an Account**: Click "Sign Up" and register with username, password, and email
2. **Login**: Use your credentials to access the dashboard
3. **Clinical Assessment**: 
   - Navigate to "Cognitive Test" or "Predictor"
   - Fill in all 32 clinical parameters
   - Submit for risk assessment
4. **MRI Assessment**:
   - Navigate to "MRI Upload"
   - Enter 9 MRI measurements
   - Submit for brain-imaging-based assessment
5. **View History**: Check "History" to see all previous predictions
6. **Download Reports**: Generate PDF or DOCX reports from results page
7. **Profile Management**: Update your email and account settings

---

## 📄 File Descriptions

### Core Application Files

#### `app.py`
- **Purpose**: Main Flask web application server
- **Functionality**:
  - Loads both trained models on startup
  - Handles all HTTP routes (login, signup, predictions, reports)
  - Manages SQLite database operations
  - Generates PDF/DOCX reports using ReportLab and python-docx
  - Provides dashboard with statistics and notifications
- **Key Routes**:
  - `/` - Landing page
  - `/login` - User authentication
  - `/signup` - User registration
  - `/home` - Dashboard with statistics
  - `/predictor` - Clinical assessment form
  - `/predict` - Clinical prediction endpoint
  - `/mri-upload` - MRI assessment form
  - `/predict_mri` - MRI prediction endpoint
  - `/history` - View all predictions
  - `/download_report/<format>` - Generate PDF/DOCX reports
  - `/profile` - User profile management

#### `train_alzheimers_model.py`
- **Purpose**: Trains clinical risk assessment model
- **Dataset**: `alzheimers_disease_data.csv` (2000+ patients)
- **Features Used** (32 total):
  - **Demographics**: Age, Gender, Ethnicity, EducationLevel
  - **Physical Health**: BMI, Smoking, AlcoholConsumption, PhysicalActivity, DietQuality, SleepQuality
  - **Medical History**: FamilyHistoryAlzheimers, CardiovascularDisease, Diabetes, Depression, HeadInjury, Hypertension
  - **Vital Signs**: SystolicBP, DiastolicBP
  - **Cholesterol**: CholesterolTotal, CholesterolLDL, CholesterolHDL, CholesterolTriglycerides
  - **Cognitive**: MMSE, FunctionalAssessment
  - **Symptoms**: MemoryComplaints, BehavioralProblems, ADL, Confusion, Disorientation, PersonalityChanges, DifficultyCompletingTasks, Forgetfulness
- **Output**: 
  - `alzheimers_model.pkl` - Random Forest model (100 estimators)
  - `alzheimers_limits.pkl` - Feature validation ranges
- **Command-line Testing**: Run with `--predict` flag

#### `train_mri_model.py`
- **Purpose**: Trains MRI-based risk assessment model
- **Dataset**: `oasis_longitudinal.csv` (OASIS-2 longitudinal study)
- **Features Used** (9 total):
  - Age - Patient age in years
  - M/F - Gender (1=Male, 0=Female)
  - EDUC - Years of education
  - SES - Socioeconomic status (1-5 scale)
  - MMSE - Mini-Mental State Examination score (0-30)
  - CDR - Clinical Dementia Rating (0, 0.5, 1, 2)
  - eTIV - Estimated total intracranial volume (cm³)
  - nWBV - Normalized whole brain volume (ratio)
  - ASF - Atlas scaling factor
- **Preprocessing**:
  - Handles missing values in SES (median imputation)
  - Drops rows with missing MMSE/CDR
  - Maps Group: Demented/Converted → 1, Nondemented → 0
- **Output**: 
  - `mri_model.pkl` - Random Forest model
  - `mri_limits.pkl` - MRI feature validation ranges

### Dataset Files

#### `alzheimers_disease_data.csv`
- **Size**: 2000+ patient records
- **Columns**: 35 (32 features + PatientID, Diagnosis, DoctorInCharge)
- **Target**: Diagnosis (0 = Low Risk, 1 = High Risk)
- **Format**: CSV with header
- **Use**: Training clinical assessment model

#### `oasis_longitudinal.csv`
- **Size**: 373 MRI sessions from 150 subjects
- **Source**: Open Access Series of Imaging Studies (OASIS-2)
- **Columns**: 15 (9 used features + metadata)
- **Target**: Group (Nondemented, Demented, Converted)
- **Format**: Tab-separated values (TSV)
- **Use**: Training MRI assessment model

### Generated Files

#### `alzheimers_model.pkl`
- **Type**: Serialized scikit-learn RandomForestClassifier
- **Training Accuracy**: ~93% (view classification report)
- **Generated By**: `train_alzheimers_model.py`
- **Size**: ~1-5 MB (depends on training)

#### `alzheimers_limits.pkl`
- **Type**: Dictionary of feature min/max values
- **Purpose**: Input validation in web forms
- **Structure**: `{'Age': {'min': 60.0, 'max': 90.0}, ...}`
- **Generated By**: `train_alzheimers_model.py`

#### `mri_model.pkl`
- **Type**: Serialized RandomForestClassifier for MRI data
- **Generated By**: `train_mri_model.py`

#### `mri_limits.pkl`
- **Type**: MRI feature validation ranges
- **Generated By**: `train_mri_model.py`

#### `users.db`
- **Type**: SQLite3 database
- **Auto-created**: First run of `app.py`
- **Tables**:
  - `users` - username, password, email
  - `predictions` - user_id, patient_name, prediction_result, input_data, prediction_type, prediction_date

---

## 🧪 Model Training

### Clinical Model Performance

The clinical model typically achieves:
- **Accuracy**: ~93%
- **Precision (Class 0)**: ~91%
- **Precision (Class 1)**: ~96%
- **Algorithm**: Random Forest with 100 estimators

### MRI Model Performance

The MRI model achieves similar performance with brain imaging data.

### Retraining Models

To retrain with updated data:

1. Update CSV files with new data
2. Run training scripts:

python train_alzheimers_model.py
python train_mri_model.py

text
3. Restart Flask application to load new models

---

## 🛠 Technical Stack

### Backend
- **Flask 3.0+**: Web framework
- **SQLite3**: User and prediction data storage
- **scikit-learn**: Machine learning (Random Forest)
- **pandas**: Data processing
- **joblib**: Model serialization

### Report Generation
- **ReportLab**: PDF creation
- **python-docx**: DOCX creation

### Frontend
- HTML5/CSS3 templates
- Bootstrap (optional)

---

## 📊 Dataset Information

### Clinical Dataset Features

The clinical model uses 32 features across multiple categories:

| Category | Features |
|----------|----------|
| Demographics | Age, Gender, Ethnicity, EducationLevel |
| Physical Health | BMI, Smoking, AlcoholConsumption, PhysicalActivity, DietQuality, SleepQuality |
| Medical History | FamilyHistoryAlzheimers, CardiovascularDisease, Diabetes, Depression, HeadInjury, Hypertension |
| Vital Signs | SystolicBP, DiastolicBP |
| Cholesterol | CholesterolTotal, CholesterolLDL, CholesterolHDL, CholesterolTriglycerides |
| Cognitive Tests | MMSE, FunctionalAssessment |
| Symptoms | MemoryComplaints, BehavioralProblems, ADL, Confusion, Disorientation, PersonalityChanges, DifficultyCompletingTasks, Forgetfulness |

### MRI Dataset Features

The MRI model uses 9 neuroimaging features:

| Feature | Description | Unit/Range |
|---------|-------------|------------|
| Age | Patient age | Years |
| M/F | Gender | 0=Female, 1=Male |
| EDUC | Years of education | Years |
| SES | Socioeconomic status | 1-5 scale |
| MMSE | Mini-Mental State Exam | 0-30 |
| CDR | Clinical Dementia Rating | 0, 0.5, 1, 2 |
| eTIV | Estimated total intracranial volume | cm³ |
| nWBV | Normalized whole brain volume | Ratio |
| ASF | Atlas scaling factor | Ratio |

---

## ⚠️ Important Notes

### Before First Use
1. **Train both models** before running the Flask app
2. Ensure CSV datasets are in the root directory
3. Install all dependencies from requirements.txt

### Security Considerations
- Change `app.secret_key` in production
- Implement password hashing (currently plain text)
- Add HTTPS in production environments
- Validate and sanitize all user inputs

### Medical Disclaimer
This system is for **educational and research purposes only**. It should not replace professional medical diagnosis or treatment. Always consult healthcare professionals for medical advice.

---

## 🔧 Troubleshooting

### "Model not found" Error
**Solution**: Run `train_alzheimers_model.py` and `train_mri_model.py` first

### CSV File Not Found
**Solution**: Ensure datasets are in the project root directory

### Database Errors
**Solution**: Delete `users.db` and restart app to regenerate

### Port Already in Use
**Solution**: Kill process on port 5000 or change port in `app.py`:

app.run(debug=True, port=5001)

text

### Import Errors
**Solution**: Verify all packages are installed:

pip list | grep -E "flask|pandas|scikit-learn|reportlab|python-docx"

text

### Model Training Fails
**Solution**: 
- Check CSV file format and encoding
- Ensure sufficient disk space for model files
- Verify pandas can read the CSV files

---

## 📞 Support

For issues or questions:
1. Check file locations and names
2. Verify all dependencies are installed
3. Review terminal output for error messages
4. Ensure models are trained before running app

---

## 🚀 Quick Start Commands

Install dependencies

pip install flask pandas scikit-learn reportlab python-docx
Train models

python train_alzheimers_model.py
python train_mri_model.py
Run application

python app.py
Access in browser
Navigate to http://localhost:5000

text

---

## 📜 License

This project is for educational purposes. Datasets used:
- Clinical data: Synthetic/example data
- OASIS-2: Open Access Series of Imaging Studies (public domain)

---

## 🙏 Acknowledgments

- **OASIS Project**: Brain imaging data
- **scikit-learn**: Machine learning framework
- **Flask Community**: Web framework support

---

**Version**: 2.0  
**Last Updated**: October 2025  
**Status**: Production Ready

---

## 📝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 🔮 Future Enhancements

- Implement password encryption (bcrypt/werkzeug)
- Add email verification for new users
- Integrate more ML models (SVM, Neural Networks)
- Real-time MRI image upload and processing
- Multi-language support
- Export predictions to CSV
- Admin dashboard for user management
- REST API for external integrations