import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Load data from CSV
df = pd.read_csv('data/radio-data.csv')

analyzer = SentimentIntensityAnalyzer()

# Analyze sentiment (compound score)
df['emotion'] = df['message'].apply(lambda msg: analyzer.polarity_scores(msg)['compound'])

print(df)
