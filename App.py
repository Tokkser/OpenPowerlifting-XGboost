import streamlit as st
import pandas as pd
import xgboost as xgb

st.title("Powerlifting performance predictor")
@st.cache_resource
def loadmodels():
    m1=xgb.XGBRegressor()
    m1.load_model('deadlift_model.json')
    m2=xgb.XGBRegressor()
    m2.load_model('squat_model.json')
    m3=xgb.XGBRegressor()
    m3.load_model('bench_model.json')
    return m1,m2,m3
dl_model,sq_model,bp_model=loadmodels()

st.sidebar.header("Information")
category= st.sidebar.selectbox("Estimate for:", ["Deadlift", "Squat", "Bench Press"])
age= st.sidebar.number_input('Age', 8,100,21)
sex=st.sidebar.selectbox("Sex", ["Male","Female"])
sexval= 1 if sex =="Male" else 2
bw = st.sidebar.number_input("Bodyweight (Kg): ",20.0,300.0,80.0)

if category== "Deadlift" :
    sq= st.number_input=("Squat 1RM (Kg):",0.0,600.0,120.0)
    bp= st.number_input=("Squat 1RM (Kg):",0.0,370.0,100.0)
    if st.button("Predict Deadlift"):
        data=pd.DataFrame([[age, sexval, bw, sq, bp]], columns=['Age', 'Sex', 'BodyweightKg', 'Best3SquatKg', 'Best3BenchKg'])
        pred= dl_model.predict(data)[0]
        st.success(f'estimated deadlift: {pred:.1f} kg')
elif category== "Squat" :
    dl= st.number_input=("Deadlift 1RM (Kg):",0.0,520.0,140.0)
    bp= st.number_input=("Bench Press 1RM (Kg):",0,370.0,100.0)
    if st.button("Predict Squat"):
        data=pd.DataFrame([[age, sexval, bw, bp, dl]], columns=['Age', 'Sex', 'BodyweightKg', 'Best3BenchKg', 'Best3DeadliftKg'])
        pred= sq_model.predict(data)[0]
        st.success(f'estimated Squat: {pred:.1f} kg')
else: 
    sq = st.number_input("Squat 1RM (kg)", 0.0, 500.0, 120.0)
    dl = st.number_input("Deadlift 1RM (kg)", 0.0, 500.0, 150.0)
    if st.button("Predict Bench"):
        data = pd.DataFrame([[age, sexval, bw, sq, dl]], columns=['Age', 'Sex', 'BodyweightKg', 'Best3SquatKg', 'Best3DeadliftKg'])
        pred = bp_model.predict(data)[0]
        st.success(f"Estimated Bench: {pred:.1f} kg")
        
    



    

