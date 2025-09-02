#A project to map drivers emotions over the race by their radio messages
#Created by: Jessica Parkes
#Started: 20/06/25


import streamlit as st
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
import plotly.express as px

st.title("F1 Race Radio Emotion Analysis - Silverstone 2025")

@st.cache_data
def load_data():
    df = pd.read_csv('data/radio-data.csv')
    analyser = SentimentIntensityAnalyzer()
    df['emotion'] = df['message'].apply(lambda msg: analyser.polarity_scores(msg)['compound'])
    df['driver'] = df['driver'].str.strip()

    def label(score):
        if score >= 0.05:
            return "Positive"
        elif score <= -0.05:
            return "Negative"
        else:
            return "Neutral"

    df["emotion_label"] = df["emotion"].apply(label)
    return df

df = load_data()

drivers = df['driver'].unique()
selected_drivers = st.multiselect("Select Drivers", drivers, default=[drivers[0]])

# Filter data by selected driver
filtered = df[df['driver'].isin(selected_drivers)]

if not filtered.empty:
    st.subheader("📈 Emotion Over Laps")
    fig = px.scatter(
        filtered,
        x="lap",
        y="emotion",
        color="driver",                  # different colour per driver
        symbol="driver",
        hover_data=["message", "lap", "emotion_label"],  # show radio message on hover
        labels={"lap": " Lap ", "emotion": " Emotion Score ", "emotion_label": " Emotion ", "message": " Radio ", "driver": " Driver "}
    )

    # Connect the dots with lines
    fig.update_traces(mode="lines+markers")

    st.plotly_chart(fig, use_container_width=True)

    if selected_drivers:
        st.subheader("📝 Driver Summaries")

        for driver in selected_drivers:
            d = filtered[filtered["driver"] == driver]

            # skip if no rows (safety check)
            if d.empty:
                continue

            peak_pos = d.loc[d["emotion"].idxmax()]
            peak_neg = d.loc[d["emotion"].idxmin()]
            avg = d["emotion"].mean()

            st.markdown(f"### {driver}")
            st.write(f"**Most Positive (Lap {peak_pos['lap']}):** {peak_pos['message']}")
            st.write(f"**Most Negative (Lap {peak_neg['lap']}):** {peak_neg['message']}")
            st.write(f"**Average Emotion Score:** {avg:.2f}")