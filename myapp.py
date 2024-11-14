import streamlit as st
import pickle
import pandas as pd

# Load the model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

# Title of the app
st.title('Liver Disease Model Deployment with Streamlit')

# Input fields for features
feature1 = st.number_input('Age of the patient')
feature2 = st.text_input('Gender of the patient')
feature3 = st.number_input('Total Bilirubin')
feature4 = st.number_input('Direct Bilirubin')
feature5 = st.number_input('Sgot Aspartate Aminotransferase')
feature6 = st.number_input('Total Proteins')
feature7 = st.number_input('A/G Ratio Albumin and Globulin Ratio')
feature8 = st.number_input('Sgpt Alkaline Phosphotase')
feature9 = st.number_input('ALB Albumin')
feature10 = st.number_input('Alkphos Alkaline Phosphotase')

# Button to make predictions
if st.button('Predict'):
    # Prepare the input data
    input_data = {
        'Age of the patient': [feature1],
        'Gender of the patient': [feature2],
        'Total Bilirubin': [feature3],
        'Direct Bilirubin': [feature4],
        'Sgot Aspartate Aminotransferase': [feature5],
        'Total Protiens': [feature6],
        'A/G Ratio Albumin and Globulin Ratio': [feature7],
        'Sgpt Alkaline Phosphotase': [feature8],
        'ALB Albumin': [feature9],
        'Alkphos Alkaline Phosphotase':[feature10]
    }
    
    # Convert to pandas DataFrame
    input_df = pd.DataFrame(input_data)
    
    # Make prediction
    prediction = model.predict(input_df)
    
    # Display the prediction
    st.write(f'The predicted class label is: {prediction[0]}')

# Run the app using the command: streamlit run app.py
