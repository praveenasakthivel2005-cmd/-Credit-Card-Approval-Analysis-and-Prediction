from pyexpat import model

import streamlit as st
import pandas as pd
import joblib

## ====================
# PAGE CONFIGURATION
# =====================

st.set_page_config(
    page_title="Credit Card Approval Prediction",
    page_icon="💳",
    layout="wide"
)

# =====================
# LOAD TRAINED MODEL
# =====================
@st.cache_resource
def load_model():
    return joblib.load("C:/Users/Admin/Downloads/Credit Card Approvall(ML)/Credit_Card_Approval_Model.pkt")

try:
    model = load_model()
except Exception as e:
    st.error(
        "Model file not found. Please keep "
        "Credit_Card_Approval_Model.pkt "
        "in the same folder as app.py."
    )
    st.stop()
# ===========
# HEADER
# ===========

st.title("CREDIT CARD APPROVAL PREDICTION")
st.write(
    "Enter applicant information to generate"
    "a prediction using the trained Machine Learning Model."
)

# =========================
# APPLICANT DETAILS FORM
# =========================

with st.form("applicant_form"):
    st.subheader(" Personal Information")
    col1, col2, col3 = st.columns(3)
    with col1:
         gender = st.selectbox(
              "Gender", ["F","M"]
         )

         age = st.number_input(
              "Age(Years)",
              min_value=18,
              max_value=100,
              value=30
         )

         education = st.selectbox(
             "Education",
             [
                 "Secondary / secondary special",
                 "Higher education",
                 "Incompleted higher",
                 "Lower seconadry",
                 "Academic degree"
             ]
         )

    with col2:
         family_status = st.selectbox(
              "Family Status",
              [
                   "Married",
                   "Single/ not married",
                   "Civilmarriage",
                   "Separated",
                   "Widow"
              ]
         )

         Children = st.number_input(
             "Number of Children",
             min_value=0,
             max_value=20,
             value=0
         )

         family_income = st.number_input(
              "Total Family Members",
              min_value=1,
              max_value=30,
              value=2
         )

    with col3:
         own_car = st.selectbox(
              "Own a car?",[1,0]
        )

         own_realty = st.selectbox(
              "Own Property?",[1,0]
         )

         housing = st.selectbox(
              "Housing Type",
              [
                   "House / apartment",
                   "Rented apartment",
                   "With parents",
                   "Municipal apartment",
                   "Office apartment",
                   "Co-op apartment"
              ]
         )

    st.divider()
    st.subheader("💰 Employment & Financial Information")  
    col4, col5, col6 = st.columns(3)

    with col4:
         income = st.number_input(
              "Total Annual Income (Dataset Units)",
              min_value=0,
              value=250000,
              step=10000
         )

         income_type = st.selectbox(
              "Income Type",
              [
                   "Working",
                   "Commercial associate",
                   "State servant",
                   "Pensioner",
                   "Student"
              ]
         )
    with col5:
         job = st.selectbox(
              "Job Title",
              [
                   "Laborers",
                   "Core staff",
                   "Accountants",
                   "Managers",
                   "Drivers",
                   "Sales staff",
                   "Security staff",
                   "High skill tech staff",
                   "Medicine staff",
                   "Other"
              ]
         )

         work_years= st.number_input(
              "Years of Working",
              min_value=0,
              max_value=60,
              value=5
         )


    with col6:
         total_bad_debt = st.number_input(
              "Total Bad Debt",
              min_value=0,
              value=0
         )

         total_good_debt = st.number_input(
              "Total Good Debt",
              min_value=0,
              value=0
         )

    st.divider()
    st.subheader("📱 Contact Information")
    col7, col8, col9 = st.columns(3)

    with col7:
         mobile = st.selectbox(
              "Own Mobile Phone?",[1,0]
         )
    with col8:
        work_phone = st.selectbox(
            "Own Work Phone?", [1, 0]
        )
    with col9:
        phone = st.selectbox(
            "Own Phone?", [1, 0]
        )

    email = st.selectbox(
        "Own Email?", [1, 0]
    )

    submitted = st.form_submit_button(
        "🔍 Predict Approval",
        use_container_width=True
    )


# ============
# PREDICTION
# ============

if submitted:

    applicant = pd.DataFrame([{
        "Applicant_Gender": gender,
        "Owned_Car": own_car,
        "Owned_Realty": own_realty,
        "Total_Children": Children,
        "Total_Income": income,
        "Income_Type": income_type,
        "Education_Type": education,
        "Family_Status": family_status,
        "Housing_Type": housing,
        "Owned_Mobile_Phone": mobile,
        "Owned_Work_Phone": work_phone,
        "Owned_Phone": phone,
        "Owned_Email": email,
        "Job_Title": job,
        "Total_Family_Members": family_income,
        "Applicant_Age": age,
        "Years_of_Working": work_years,
        "Total_Bad_Debt": total_bad_debt,
        "Total_Good_Debt": total_good_debt
    }])

    try:
        # Use the complete applicant input
        input_data = applicant.copy()

        # Predict
        prediction = model.predict(input_data)

        if prediction[0] == 1:
            st.success("Credit Card Application Approved! ✅")
        else:
            st.error("Credit Card Application Rejected! ❌")

    except Exception as e:
        st.error(f"Prediction failed: {e}")



