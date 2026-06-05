import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Candidate Ranking")

# =====================================
# Load Ranked Candidates
# =====================================

df = pd.read_csv(
    "../data/processed/ranked_candidates.csv"
)

# =====================================
# Dashboard Metrics
# =====================================

col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Ranked Candidates",
    len(df)
)

col2.metric(
    "Top Candidate",
    df.iloc[0]["candidate_id"]
)

col3.metric(
    "Best TOPSIS Score",
    round(
        df["topsis_score"].max(),
        4
    )
)

# =====================================
# Filter
# =====================================

st.subheader("Ranking Filter")

top_n = st.slider(
    "Show Top N Candidates",
    min_value=5,
    max_value=100,
    value=20,
    step=5
)

candidate_search = st.text_input(
    "Search Candidate ID"
)

filtered_df = df.copy()

if candidate_search:

    filtered_df = filtered_df[
        filtered_df["candidate_id"]
        .str.contains(
            candidate_search,
            case=False
        )
    ]

filtered_df = filtered_df.head(
    top_n
)

# =====================================
# Ranking Table
# =====================================

st.subheader("Candidate Ranking")

st.dataframe(
    filtered_df[
        [
            "rank",
            "candidate_id",
            "gpa",
            "gmat",
            "work_exp",
            "ml_probability",
            "topsis_score"
        ]
    ].reset_index(drop=True),
    use_container_width=True
)

# =====================================
# TOP 10 Chart
# =====================================

st.subheader("Top 10 TOPSIS Scores")

top10 = df.head(10)

fig = px.bar(
    top10,
    x="candidate_id",
    y="topsis_score"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# =====================================
# Download
# =====================================

csv = df.to_csv(
    index=False
).encode("utf-8")

st.download_button(
    label="📥 Download Ranking CSV",
    data=csv,
    file_name="ranked_candidates.csv",
    mime="text/csv"
)