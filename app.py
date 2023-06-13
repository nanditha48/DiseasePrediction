import pickle
import streamlit as st 
from streamlit_option_menu import option_menu
import os
os.environ['NUMEXPR_MAX_THREADS'] = '4' # or however many threads you want to use

#loading our saved models
diabetes_models = pickle.load(open('C:/Users/91898/OneDrive/Desktop/Multiple Disease Prediction System/Saved Models/diabetes_model.sav','rb'))
heart_disease_models = pickle.load(open('C:/Users/91898/OneDrive/Desktop/Multiple Disease Prediction System/Saved Models/heart_disease_model.sav','rb'))
parkinsons_model = pickle.load(open('C:/Users/91898/OneDrive/Desktop/Multiple Disease Prediction System/Saved Models/parkinsons_model.sav','rb'))
breastcancer_model =pickle.load(open('C:/Users/91898/OneDrive/Desktop/Multiple Disease Prediction System/Saved Models/breastcancer_model.sav','rb'))

#sidebar for nav
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction using Machine Learning Website',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction',
                            'Breast Cancer Prediction'],
                            icons =['activity','heart','person-fill','person'],
                             default_index=0)

#Diabetes prediction page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction using ML')
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.number_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.number_input('Glucose Level')
    
    with col3:
        BloodPressure = st.number_input('Blood Pressure value')
    
    with col1:
        SkinThickness = st.number_input('Skin Thickness value')
    
    with col2:
        Insulin = st.number_input('Insulin Level')
    
    with col3:
        BMI = st.number_input('BMI value')
    
    with col1:
        DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function value')
    
    with col2:
        Age = st.number_input('Age of the Person')

    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_models.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'The person is diabetic'
        else:
          diab_diagnosis = 'The person is not diabetic'
        
    st.success(diab_diagnosis)

#Heart Disease 
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction using ML')
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.number_input('Age')
        
    with col2:
        sex = st.number_input('Sex')
        
    with col3:
        cp = st.number_input('Chest Pain types')
        
    with col1:
        trestbps = st.number_input('Resting Blood Pressure')
        
    with col2:
        chol = st.number_input('Serum Cholestoral in mg/dl')
        
    with col3:
        fbs = st.number_input('Fasting Blood Sugar > 120 mg/dl')
        
    with col1:
        restecg = st.number_input('Resting Electrocardiographic results')
        
    with col2:
        thalach = st.number_input('Maximum Heart Rate achieved')
        
    with col3:
        exang = st.number_input('Exercise Induced Angina')
        
    with col1:
        oldpeak = st.number_input('ST depression induced by exercise')
        
    with col2:
        slope = st.number_input('Slope of the peak exercise ST segment')
        
    with col3:
        ca = st.number_input('Major vessels colored by flourosopy')
        
    with col1:
        thal = st.number_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_models.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)


#Parkinsons Disease
if (selected == 'Parkinsons Prediction'):
    
    # page title
    st.title('Parkinsons Prediction using ML')
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        fo = st.number_input('MDVP:Fo(Hz)')
        
    with col2:
        fhi = st.number_input('MDVP:Fhi(Hz)')
        
    with col3:
        flo = st.number_input('MDVP:Flo(Hz)')
        
    with col4:
        Jitter_percent = st.number_input('MDVP:Jitter(%)')
        
    with col5:
        Jitter_Abs = st.number_input('MDVP:Jitter(Abs)')
        
    with col1:
        RAP = st.number_input('MDVP:RAP')
        
    with col2:
        PPQ = st.number_input('MDVP:PPQ')
        
    with col3:
        DDP = st.number_input('Jitter:DDP')
        
    with col4:
        Shimmer = st.number_input('MDVP:Shimmer')
        
    with col5:
        Shimmer_dB = st.number_input('MDVP:Shimmer(dB)')
        
    with col1:
        APQ3 = st.number_input('Shimmer:APQ3')
        
    with col2:
        APQ5 = st.number_input('Shimmer:APQ5')
        
    with col3:
        APQ = st.number_input('MDVP:APQ')
        
    with col4:
        DDA = st.number_input('Shimmer:DDA')
        
    with col5:
        NHR = st.number_input('NHR')
        
    with col1:
        HNR = st.number_input('HNR')
        
    with col2:
        RPDE = st.number_input('RPDE')
        
    with col3:
        DFA = st.number_input('DFA')
        
    with col4:
        spread1 = st.number_input('spread1')
        
    with col5:
        spread2 = st.number_input('spread2')
        
    with col1:
        D2 = st.number_input('D2')
        
    with col2:
        PPE = st.number_input('PPE')
        
    
    
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        
        if (parkinsons_prediction[0] == 1):
          parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
          parkinsons_diagnosis = "The person does not have Parkinson's disease"
        
    st.success(parkinsons_diagnosis)

#Breast Cancer Disease
if (selected == 'Breast Cancer Prediction'):
    
    # page title
    st.title('Breast Cancer Prediction using ML')
    col1, col2, col3, col4, col5 = st.columns(5) 
    
    with col1:
        mr = st.number_input('mean radius')
        
    with col2:
        mt = st.number_input('mean texture')
        
    with col3:
        mp = st.number_input('mean perimeter')
        
    with col4:
        ma = st.number_input('mean area')
        
    with col5:
        ms = st.number_input('mean smoothness')
        
    with col1:
        mc = st.number_input('mean compactness')
        
    with col2:
        mco = st.number_input('mean concavity')
        
    with col3:
        mcp = st.number_input('mean concave points')
        
    with col4:
        msym = st.number_input('mean symmetry')
        
    with col5:
        mfd = st.number_input('mean fractal dimension')
        
    with col1:
        re = st.number_input('radius error')
        
    with col2:
        te = st.number_input('texture error')
        
    with col3:
        pe = st.number_input('perimeter error')
        
    with col4:
        ae = st.number_input('area error')
        
    with col5:
        se = st.number_input('smoothness error')
        
    with col1:
        ce = st.number_input('compactness error')
        
    with col2:
        coe = st.number_input('concavity error')
        
    with col3:
        cpe = st.number_input('concave points error')
        
    with col4:
        sye = st.number_input('symmetry error')
        
    with col5:
        fde = st.number_input('fractal dimension error')
        
    with col1:
        wr = st.number_input('worst radius')
        
    with col2:
        wt = st.number_input('worst texture')

    with col3:
        wp = st.number_input('worst perimeter')
        
    with col4:
        wa = st.number_input('worst area')
        
    with col5:
        ws = st.number_input('worst smoothness')

    with col1:
        wc = st.number_input('worst compactness')
        
    with col2:
        wco = st.number_input('worst concavity')

    with col3:
        wcp = st.number_input('worst concave points')
        
    with col4:
        wsy = st.number_input('worst symmetry')
        
    with col5:
        wfd = st.number_input('worst fractal dimension')

    # code for Prediction
    breastcancer_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Breast Cancer Test Result"):
        breastcancer_prediction = breastcancer_model.predict([[mr, mt, mp, ma, ms, mc, mco, mcp, msym, mfd, re, te, pe, ae, se, ce, coe, cpe, sye, fde, wr, wp, wt, wa, ws, wc, wco, wcp, wsy, wfd]])                          
        
        if (breastcancer_prediction[0] == 1):
          breastcancer_diagnosis = "The breast cancer is Benign"
        else:
          breastcancer_diagnosis = "The breast cancer is Malignant"
        
    st.success(breastcancer_diagnosis)

