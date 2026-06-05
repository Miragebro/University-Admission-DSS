import streamlit as st
import pandas as pd
import joblib

st.title("Scenario Testing")

pipeline = joblib.load(
    "../models/best_model.pkl"
)

# =====================================
# Scenario Selection
# =====================================

scenario = st.selectbox(
    "Choose Scenario",
    [
        "High Potential Applicant",
        "Low Potential Applicant",
        "Average Applicant"
    ]
)

# =====================================
# Scenario Data
# =====================================

if scenario == "High Potential Applicant":

    data = {
        "international": 1,
        "gpa": 3.4,
        "major": "Business",
        "gmat": 720,
        "work_exp": 5,
        "work_industry": "Investment Banking"
    }

elif scenario == "Low Potential Applicant":

    data = {
        "international": 0,
        "gpa": 2.8,
        "major": "Humanities",
        "gmat": 580,
        "work_exp": 2,
        "work_industry": "Retail"
    }

else:

    data = {
        "international": 0,
        "gpa": 3.8,
        "major": "STEM",
        "gmat": 760,
        "work_exp": 6,
        "work_industry": "Consulting"
    }

# =====================================
# Feature Engineering
# =====================================

academic_index = (
    data["gpa"] * 100
    + data["gmat"] / 10
)

if data["work_exp"] <= 3:
    experience_level = "Junior"
elif data["work_exp"] <= 6:
    experience_level = "Mid"
else:
    experience_level = "Senior"

gpa_gmat_score = (
    data["gpa"]
    * data["gmat"]
)

input_df = pd.DataFrame({
    "international": [data["international"]],
    "gpa": [data["gpa"]],
    "major": [data["major"]],
    "gmat": [data["gmat"]],
    "work_exp": [data["work_exp"]],
    "work_industry": [data["work_industry"]],
    "academic_index": [academic_index],
    "experience_level": [experience_level],
    "gpa_gmat_score": [gpa_gmat_score]
})

# =====================================
# Show Scenario
# =====================================

st.subheader("Scenario Data")

st.dataframe(
    input_df.reset_index(drop=True),
    use_container_width=True
)

# =====================================
# Run Test
# =====================================

if st.button("Run Scenario"):

    prediction = pipeline.predict(
        input_df
    )[0]

    probability = pipeline.predict_proba(
        input_df
    )[0][1]

    st.subheader(
        "Scenario Result"
    )

    if prediction == 1:

        st.success(
            "Recommended for Admission"
        )

    else:

        st.error(
            "Not Recommended for Admission"
        )

    st.metric(
        "Admission Probability",
        f"{probability:.2%}"
    )