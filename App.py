import streamlit as st
import pandas as pd
import xgboost as xgb
import plotly.graph_objects as go
st.set_page_config(page_title="PR Predictor", page_icon="🏋️‍♂️", layout="centered")
tab1,tab2= st.tabs(['Lift Prediction Engine','Leverage Analysis'])
st.sidebar.header("Information")
category= st.sidebar.selectbox("Estimate for:", ["Deadlift", "Squat", "Bench Press"])
age= st.sidebar.number_input('Age', 8.0,100.0,21.0, step=1.0)
sex=st.sidebar.selectbox("Sex", ["Male","Female"])
sexval= 1 if sex =="Male" else 2
bw = st.sidebar.number_input("Bodyweight (Kg): ",20.0,300.0,80.0, step= 1.0)
with tab1:
    st.header('Lift Prediction')
    st.markdown("""
        <style>
        .main { background-color: #f5f7f9; }
        .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #ff4b4b; color: white; }
        .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
        </style>
        """, unsafe_allow_html=True)
    st.title("Powerlifting Performance Predictor")
    st.write("Enter your stats below to estimate your expected lift.")
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


    if category== "Deadlift" :
        sq = st.number_input("Squat 1RM (Kg):", min_value=0.0, max_value=600.0, value=120.0, step=5.0,key='dltab1')
        bp = st.number_input("Bench 1RM (Kg):", min_value=0.0, max_value=370.0, value=100.0, step= 5.0,key='dltab1')
        dlift= st.number_input("Enter your actual deadlift:", min_value=0.0, max_value=510.0, value=100.0, step= 5.0,key='dltab1')
        if st.button("Predict Deadlift"):
            data=pd.DataFrame([[age, sexval, bw, sq, bp]], columns=['Age', 'Sex', 'BodyweightKg', 'Best3SquatKg', 'Best3BenchKg']).astype(float)
            pred= dl_model.predict(data)[0]
            st.success(f'Estimated deadlift: {pred:.1f} kg')
            st.progress(float(min(pred / 510.0, 1.0)),text=f'That is {(pred/5.10):.2f} % of the world record')
            with st.container(border=True):
                value=round((dlift*100/pred),2)
                st.write(f'Performance Analysis')
                st.metric('Actual Performance vs Estimated Performance', f'{value:.2f} %',f'{(dlift-pred):.2f} Kg')
            if value>=100:
                st.success(f"Well done your Deadlift is truly magnificient")
            elif value<=80:
                st.success(f'Dissapointed?, Perhaps your leverages are well suited for some other lift')
            else:
                st.success(f'Keep it up!')
    elif category== "Squat" :
        dl = st.number_input("Deadlift 1RM (Kg):", min_value=0.0, max_value=520.0, value=140.0, step=5.0,key='dltab1')
        bp = st.number_input("Bench Press 1RM (Kg):", min_value=0.0, max_value=370.0, value=100.0, step=5.0,key='dltab1')
        sqt = st.number_input("Enter your Actual Squat (kg)", min_value=0.0, max_value=500.0, value=120.0, step=5.0,key='dltab1')
        if st.button("Predict Squat"):
            data=pd.DataFrame([[age, sexval, bw, bp, dl]], columns=['Age', 'Sex', 'BodyweightKg', 'Best3BenchKg', 'Best3DeadliftKg']).astype(float)
            pred= sq_model.predict(data)[0]
            st.success(f'Estimated Squat: {pred:.1f} kg')
            st.progress(float(min(pred / 490.0, 1.0)),text=f'That is {(pred/4.90):.2f} % of the world record')
            with st.container(border=True):
                value=round((sqt*100/pred),2)
                st.write(f'Performance Analysis')
                st.metric('Actual Performance vs Estimated Performance', f'{value:.2f} %',f'{(sqt-pred):.2f} Kg')
            if value>=100:
                st.success(f"Well done your Squat is truly magnificient")
            elif value<=80:
                st.success(f'Dissapointed?, Perhaps your leverages are well suited for some other lift')
            else:
                st.success(f'Keep it up!')
    else: 
        sq = st.number_input("Squat 1RM (kg)", min_value=0.0, max_value=500.0, value=120.0, step=5.0,key='dltab1')
        dl = st.number_input("Deadlift 1RM (kg)", min_value=0.0, max_value=500.0, value=150.0, step=5.0,key='dltab1')
        bpc= st.number_input("Enter your Actual Bench Press (Kg):", min_value=0.0, max_value=370.0, value=100.0, step=5.0,key='dltab1')
        if st.button("Predict Bench"):
            data = pd.DataFrame([[age, sexval, bw, sq, dl]], columns=['Age', 'Sex', 'BodyweightKg', 'Best3SquatKg', 'Best3DeadliftKg']).astype(float)
            pred = bp_model.predict(data)[0]
            st.success(f"Estimated Bench: {pred:.1f} kg")
            st.progress(float(min(pred / 360.0, 1.0)),text=f'That is {(pred/3.60):.2f} % of the world record')
            with st.container(border=True):
                value=round((bpc*100/pred),2)
                st.write(f'Performance Analysis')
                st.metric('Actual Performance vs Estimated Performance', f'{value:.2f} %',f'{(bpc-pred):.2f} Kg')
            if value>=100:
                st.success(f"Well done your Bench Press is truly magnificient")
            elif value<=80:
                st.success(f'Dissapointed?, Perhaps your leverages are well suited for some other lift')
            else:
                st.success(f'Keep it up!')
                       
with tab2:
    st.header('Leverage Analysis')
    st.markdown("""
        <style>
        .main { background-color: #f5f7f9; }
        .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #ff4b4b; color: white; }
        .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
        </style>
        """, unsafe_allow_html=True)
    st.title("Powerlifting Leverage Analysis")
    st.write("Enter your stats below to analyze your leverages.")
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
    dl = st.number_input("Deadlift 1RM (Kg):", min_value=0.0, max_value=520.0, value=140.0, step=5.0)
    bp = st.number_input("Bench Press 1RM (Kg):", min_value=0.0, max_value=370.0, value=100.0, step=5.0)
    sqt = st.number_input("Squat 1RM (kg)", min_value=0.0, max_value=500.0, value=120.0, step=5.0)
    
    if st.button('Analyse my Leverages'):
        dlpred= dl_model.predict(pd.DataFrame([[age, sexval, bw, sqt, bp]], columns=['Age', 'Sex', 'BodyweightKg', 'Best3SquatKg', 'Best3BenchKg']).astype(float))[0]
        sqpred= sq_model.predict(pd.DataFrame([[age, sexval, bw, bp, dl]], columns=['Age', 'Sex', 'BodyweightKg', 'Best3BenchKg', 'Best3DeadliftKg']).astype(float))[0]
        bppred= bp_model.predict(pd.DataFrame([[age, sexval, bw, sq, dl]], columns=['Age', 'Sex', 'BodyweightKg', 'Best3SquatKg', 'Best3DeadliftKg']).astype(float))[0]
        dlratio=dl*100/dlpred
        sqratio=sqt*100/sqpred
        bpratio=bp*100/bppred
    
        st.metric(f'Actual Deadlift vs Predicted Deadlift',f'{(dlratio-100):.2f} %',f'{-1*(dlpred-dl):.2f} Kg')
        st.metric(f'Actual Squat vs Predicted Squat',f'{(sqratio-100):.2f} %',f'{-1*(sqpred-sqt):.2f} Kg')
        st.metric(f'Actual Bench vs Predicted Bench',f'{(bpratio-100):.2f} %',f'{-1*(bppred-bp):.2f} Kg')

        ratios={"Deadlift":dlratio,"Squat":sqratio,"Bench Press":bpratio}
        sortedlifts= sorted(ratios.items(), key= lambda x:x[1],reverse=True)
        max_lift,max_val= sortedlifts[0]
        second_lift,second_val=sortedlifts[1]
        bottom_lift,bottom_val=sortedlifts[2]



        gap_total = max_val - bottom_val
        gap_specialist = max_val - second_val

        if gap_total <= 10:
            st.header('All-Rounder')
            st.success('You are balanced, No single leverage overshadows another')

        elif gap_specialist > 12:
            st.header(f'The {max_lift} Specialist')
            st.success(f'Your {max_lift} is truly magnificent and far exceeds your other lifts.')

        elif gap_total > 10:
            if max_lift in ['Squat', 'Deadlift'] and second_lift in ['Squat', 'Deadlift']:
                st.header('The Strongman Hybrid')
                st.success('Your lower body leverages are elite, but your bench is a mechanical weak point.')
            
            elif max_lift in ['Deadlift','Bench Press'] and second_lift in ['Deadlift','Bench Press']:
                st.header('The Gorilla Build')
                st.success('Long arms favor your pull and your wingspan helps your bench drive, but squats are a struggle.')

            elif max_lift in ['Squat', 'Bench Press'] and second_lift in ['Squat', 'Bench Press']:
                st.header('The Short-Lever Powerhouse')
                st.success('You are built to push weight. You excel at Squat and Bench, while Deadlift is your challenge.')

        categ = ['Deadlift', 'Squat', 'Bench Press']
        rvalues = [float(dlratio), float(sqratio), float(bpratio), float(dlratio)]
        theta = categ + [categ[0]]
        fig = go.Figure()
        fig.add_trace(go.Scatterpolar(r=rvalues,theta=theta,fill='toself',name='Your Profile',line=dict(color='green'),marker=dict(size=8)))
        fig.update_layout(showlegend=True)
        st.plotly_chart(fig)
                
                

               
        

            

    



    












































