import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

# Load and preprocess data
@st.cache_data
def load_data():
    # Load dataset
    data = pd.read_csv('student.csv')
    
    # Store all label encoders and unique values
    label_encoders = {}
    unique_values = {}
    
    # Preprocessing
    categorical_cols = data.select_dtypes(include=['object']).columns
    for col in categorical_cols:
        if col != 'Status':  # We'll encode the target separately
            le = LabelEncoder()
            data[col] = le.fit_transform(data[col].astype(str))
            label_encoders[col] = le
            # Get unique values correctly
            unique_values[col] = le.classes_
    
    # Encode target variable
    le_status = LabelEncoder()
    data['Status_encoded'] = le_status.fit_transform(data['Status'])
    
    return data, label_encoders, unique_values, le_status

try:
    data, label_encoders, unique_values, le_status = load_data()
except Exception as e:
    st.error(f"Error loading data: {str(e)}")
    st.stop()

# Split data into features and target
X = data.drop(['Status', 'Status_encoded'], axis=1)
y = data['Status_encoded']

# Train model
@st.cache_resource
def train_model():
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    return model, accuracy

model, accuracy = train_model()

# Streamlit UI
st.title('Student Dropout Prediction Prototype')
st.write('Predict student outcomes based on academic and demographic information.')

# Input form
with st.form("student_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        marital_status = st.selectbox('Marital Status', unique_values['Marital_status'])
        application_mode = st.selectbox('Application Mode', unique_values['Application_mode'])
        course = st.selectbox('Course', unique_values['Course'])
        attendance = st.selectbox('Attendance', unique_values['Daytime_evening_attendance'])
        prev_qualification = st.selectbox('Previous Qualification', unique_values['Previous_qualification'])
        nationality = st.selectbox('Nationality', unique_values['Nacionality'])
        mothers_qual = st.selectbox("Mother's Qualification", unique_values['Mothers_qualification'])
        fathers_qual = st.selectbox("Father's Qualification", unique_values['Fathers_qualification'])
        
    with col2:
        mothers_occupation = st.selectbox("Mother's Occupation", unique_values['Mothers_occupation'])
        fathers_occupation = st.selectbox("Father's Occupation", unique_values['Fathers_occupation'])
        displaced = st.selectbox('Displaced', unique_values['Displaced'])
        special_needs = st.selectbox('Special Needs', unique_values['Educational_special_needs'])
        debtor = st.selectbox('Debtor', unique_values['Debtor'])
        tuition_up_to_date = st.selectbox('Tuition Up-to-date', unique_values['Tuition_fees_up_to_date'])
        gender = st.selectbox('Gender', unique_values['Gender'])
        scholarship = st.selectbox('Scholarship', unique_values['Scholarship_holder'])
    
    # Numerik input
    application_order = st.number_input('Application Order', min_value=0, max_value=9, value=1)
    prev_qual_grade = st.number_input('Previous Qualification Grade', min_value=0, max_value=200, value=100)
    admission_grade = st.number_input('Admission Grade', min_value=0, max_value=200, value=100)
    age_enrollment = st.number_input('Age at Enrollment', min_value=15, max_value=70, value=20)
    
    submitted = st.form_submit_button("Predict")

if submitted:
    # Menyiapkan input data
    input_data = {
        'Marital_status': marital_status,
        'Application_mode': application_mode,
        'Application_order': application_order,
        'Course': course,
        'Daytime_evening_attendance': attendance,
        'Previous_qualification': prev_qualification,
        'Previous_qualification_grade': prev_qual_grade,
        'Nacionality': nationality,
        'Mothers_qualification': mothers_qual,
        'Fathers_qualification': fathers_qual,
        'Mothers_occupation': mothers_occupation,
        'Fathers_occupation': fathers_occupation,
        'Admission_grade': admission_grade,
        'Displaced': displaced,
        'Educational_special_needs': special_needs,
        'Debtor': debtor,
        'Tuition_fees_up_to_date': tuition_up_to_date,
        'Gender': gender,
        'Scholarship_holder': scholarship,
        'Age_at_enrollment': age_enrollment,
        
    }
    
    # Buat DataFrame dan enkode variabel kategoris
    input_df = pd.DataFrame([input_data])
    for col in input_df.columns:
        if col in label_encoders:
            input_df[col] = label_encoders[col].transform(input_df[col].astype(str))
    
    # Pastikan semua kolom ada
    for col in X.columns:
        if col not in input_df.columns:
            input_df[col] = 0  
    
    # Susun ulang kolom agar sesuai dengan data pelatihan
    input_df = input_df[X.columns]
    
    # Membuat Prediksi
    try:
        prediction = model.predict(input_df)
        proba = model.predict_proba(input_df)
        
        status = le_status.inverse_transform(prediction)[0]
        confidence = proba[0][prediction[0]] * 100
        
        st.subheader('Prediction Result')
        if status == 'Dropout':
            st.error(f'Predicted: {status} ({confidence:.1f}% confidence)')
        elif status == 'Enrolled':
            st.warning(f'Predicted: {status} ({confidence:.1f}% confidence)')
        else:
            st.success(f'Predicted: {status} ({confidence:.1f}% confidence)')
            
        # Menampilkan Probabilitas
        st.subheader('Probability Distribution')
        prob_df = pd.DataFrame({
            'Status': le_status.classes_,
            'Probability': proba[0] * 100
        })
        st.bar_chart(prob_df.set_index('Status'))
        
    except Exception as e:
        st.error(f"Prediction error: {str(e)}")

# Model info
st.sidebar.header('Informasi Model')
st.sidebar.write(f"Accuracy: {accuracy:.1%}")
st.sidebar.write("Features used:", X.columns.tolist())