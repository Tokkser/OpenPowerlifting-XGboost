import streamlit as st
import pandas as pd
import xgboost as xgb
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #ff4b4b; color: white; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    </style>
    """, unsafe_allow_html=True)
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
age= st.sidebar.number_input('Age', 8.0,100.0,21.0, step=1.0)
sex=st.sidebar.selectbox("Sex", ["Male","Female"])
sexval= 1 if sex =="Male" else 2
bw = st.sidebar.number_input("Bodyweight (Kg): ",20.0,300.0,80.0, step= 1.0)

if category== "Deadlift" :
    sq = st.number_input("Squat 1RM (Kg):", min_value=0.0, max_value=600.0, value=120.0, step=5.0)
    bp = st.number_input("Bench 1RM (Kg):", min_value=0.0, max_value=370.0, value=100.0, step= 5.0)
    if st.button("Predict Deadlift"):
        data=pd.DataFrame([[age, sexval, bw, sq, bp]], columns=['Age', 'Sex', 'BodyweightKg', 'Best3SquatKg', 'Best3BenchKg']).astype(float)
        pred= dl_model.predict(data)[0]
        st.success(f'estimated deadlift: {pred:.1f} kg')
elif category== "Squat" :
    dl = st.number_input("Deadlift 1RM (Kg):", min_value=0.0, max_value=520.0, value=140.0, step=5.0)
    bp = st.number_input("Bench Press 1RM (Kg):", min_value=0.0, max_value=370.0, value=100.0, step=5.0)
    if st.button("Predict Squat"):
        data=pd.DataFrame([[age, sexval, bw, bp, dl]], columns=['Age', 'Sex', 'BodyweightKg', 'Best3BenchKg', 'Best3DeadliftKg']).astype(float)
        pred= sq_model.predict(data)[0]
        st.success(f'estimated Squat: {pred:.1f} kg')
else: 
    sq = st.number_input("Squat 1RM (kg)", min_value=0.0, max_value=500.0, value=120.0, step=5.0)
    dl = st.number_input("Deadlift 1RM (kg)", min_value=0.0, max_value=500.0, value=150.0, step=5.0)
    if st.button("Predict Bench"):
        data = pd.DataFrame([[age, sexval, bw, sq, dl]], columns=['Age', 'Sex', 'BodyweightKg', 'Best3SquatKg', 'Best3DeadliftKg']).astype(float)
        pred = bp_model.predict(data)[0]
        st.success(f"Estimated Bench: {pred:.1f} kg")
        
    



    







