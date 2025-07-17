#A project to map drivers emotions over the race by their radio messages
#Created by: Jessica Parkes
#Started: 20/06/25


import streamlit as st
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt

st.title("F1 Race Radio Emotion Analysis - Silverstone 2025")

@st.cache_data
def load_data():
    df = pd.read_csv('data/radio-data.csv')
    analyser = SentimentIntensityAnalyzer()
    df['emotion'] = df['message'].apply(lambda msg: analyser.polarity_scores(msg)['compound'])
    return df

df = load_data()

drivers = df['driver'].unique()
selected_driver = st.selectbox("Select Driver", drivers)

# Filter data by selected driver
filtered_df = df[df['driver'] == selected_driver]

st.subheader(f"Race Radio Data for {selected_driver}")
st.dataframe(filtered_df)

st.subheader(f"Emotion Over Laps for {selected_driver}")
fig, ax = plt.subplots()
ax.plot(filtered_df['lap'], filtered_df['emotion'], marker='o')
ax.set_xlabel("Lap")
ax.set_ylabel("Emotion Score")
ax.set_title(f"Emotion of Radio Messages Over Laps - {selected_driver}")
st.pyplot(fig)
