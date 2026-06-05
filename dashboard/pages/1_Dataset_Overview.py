import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Dataset Overview")

df = pd.read_csv(
    "../data/raw/MBA.csv"
)

df["admission_clean"] = (
    df["admission"]
    .fillna("Deny")
)

# =========================
# KPI Metrics
# =========================

total_applicants = len(df)

total_admit = (
    df["admission_clean"] == "Admit"
).sum()

total_waitlist = (
    df["admission_clean"] == "Waitlist"
).sum()

total_deny = (
    df["admission_clean"] == "Deny"
).sum()

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Applicants",
    total_applicants
)

col2.metric(
    "Admit",
    total_admit
)

col3.metric(
    "Waitlist",
    total_waitlist
)

col4.metric(
    "Deny",
    total_deny
)

# =========================
# Admission Distribution
# =========================

st.subheader("Admission Distribution")

fig = px.histogram(
    df,
    x="admission_clean"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# =========================
# GPA Distribution
# =========================

st.subheader("GPA Distribution")

fig = px.histogram(
    df,
    x="gpa"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# =========================
# GMAT Distribution
# =========================

st.subheader("GMAT Distribution")

fig = px.histogram(
    df,
    x="gmat"
)

st.plotly_chart(
    fig,
    use_container_width=True
)