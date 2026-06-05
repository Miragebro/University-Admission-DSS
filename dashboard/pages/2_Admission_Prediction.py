import streamlit as st
import pandas as pd
import joblib

st.title("Admission Prediction")

# =====================================
# Load Model
# =====================================

pipeline = joblib.load(
    "../models/best_model.pkl"
)

# =====================================
# Input Form
# =====================================

st.subheader("Applicant Information")

col1, col2 = st.columns(2)

with col1:

    gpa = st.number_input(
        "GPA",
        min_value=2.0,
        max_value=4.0,
        value=3.25,
        step=0.01
    )

    gmat = st.number_input(
        "GMAT",
        min_value=500,
        max_value=800,
        value=650,
        step=10
    )

    work_exp = st.number_input(
        "Work Experience (Years)",
        min_value=0,
        max_value=20,
        value=5,
        step=1
    )

with col2:

    major = st.selectbox(
        "Major",
        [
            "Business",
            "Humanities",
            "STEM"
        ]
    )

    work_industry = st.selectbox(
        "Work Industry",
        [
            "Financial Services",
            "Investment Management",
            "Technology",
            "Consulting",
            "Nonprofit/Gov",
            "PE/VC",
            "Health Care",
            "Investment Banking",
            "Other",
            "Retail",
            "Energy",
            "CPG",
            "Real Estate",
            "Media/Entertainment"
        ]
    )

    international = st.selectbox(
        "International Student",
        [
            False,
            True
        ]
    )

# =====================================
# Predict Button
# =====================================

if st.button("Predict Admission"):

    # =========================
    # Feature Engineering
    # =========================

    academic_index = (
        (gpa * 100)
        + (gmat / 10)
    )

    if work_exp <= 3:
        experience_level = "Junior"
    elif work_exp <= 6:
        experience_level = "Mid"
    else:
        experience_level = "Senior"

    gpa_gmat_score = (
        gpa * gmat
    )

    # =========================
    # Build Input DataFrame
    # =========================

    input_df = pd.DataFrame({
        "international": [int(international)],
        "gpa": [gpa],
        "major": [major],
        "gmat": [gmat],
        "work_exp": [work_exp],
        "work_industry": [work_industry],
        "academic_index": [academic_index],
        "experience_level": [experience_level],
        "gpa_gmat_score": [gpa_gmat_score]
    })

    # =========================
    # Prediction
    # =========================

    prediction = pipeline.predict(
        input_df
    )[0]

    probability = pipeline.predict_proba(
        input_df
    )[0][1]

    # =========================
    # Output
    # =========================

    st.divider()

    st.subheader("Prediction Result")

    if prediction == 1:

        st.success(
            "✅ Recommended for Admission"
        )

    else:

        st.error(
            "❌ Not Recommended for Admission"
        )

    st.metric(
        "Admission Probability",
        f"{probability:.2%}"
    )

    st.subheader("Generated Features")

    st.json(
        {
            "Academic Index": academic_index,
            "Experience Level": experience_level,
            "GPA × GMAT Score": gpa_gmat_score
        }
    )