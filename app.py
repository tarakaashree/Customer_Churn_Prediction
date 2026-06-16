import joblib
import streamlit as st
import pandas as pd

model=joblib.load('lr_model-2.joblib')
encoder=joblib.load('encoder-2.joblib')
scaler=joblib.load('scaler-2.joblib')

st.title("Customer Churn Prediction")
st.write("Please enter the following details to predict if a customer will churn:")
name=st.text_input("Name")
Gender=st.radio("Gender",['Male','Female'])
Contract=st.radio("Contract",['Month-to-month','One year','Two year'])
Tenure=st.number_input("Tenure (months(0-72))", min_value=0, max_value=72)
PaymentMethod=st.radio("Payment Method",['Electronic check','Mailed check','Bank transfer (automatic)','Credit card (automatic)'])
InternetService=st.radio("Internet Service",['DSL','Fiber optic','No'])
Tech_Support=st.radio("Tech Support",['Yes','No','No internet service'])
Prediction=st.button("Predict")
if Prediction:

    input_df = pd.DataFrame({
        "gender":[Gender],
        "InternetService":[InternetService],
        "TechSupport":[Tech_Support],
        "Contract":[Contract],
        "PaymentMethod":[PaymentMethod]
    })

    encoded = encoder.transform(input_df)

    encoded_df = pd.DataFrame(
        encoded,
        columns=encoder.get_feature_names_out()
    )

    encoded_df.insert(0, "tenure", Tenure)

    input_scaled = scaler.transform(encoded_df)

    prediction = model.predict(input_scaled)

    if prediction[0] == 1:
        st.success(f"{name} is likely to churn.")
    else:
        st.success(f"{name} is not likely to churn.")