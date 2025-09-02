# race-radio-emotion-analysis
Analysing F1 race radio emotions
A project to map drivers emotions over the race by their radio messages
Created by: Jessica Parkes
Started: 20/06/25

Features
- Loads race radio messages from CSV data  
- Performs emotion analysis using VADER  
- Interactive visualisation of emotion over laps using Plotly
- Multi-driver selection 
- Displays raw radio message data

Used:
- Python
- Streamlit
- pandas
- Matplotlib
- Plotly


How to run:
1. **Clone this repository** or download the files
2. Make sure you have Python and pip installed
3. Install dependencies: pip install streamlit pandas matplotlib plotly vaderSentiment
4. Run the Streamlit app: streamlit run app/app.py
5. Select one or more drivers to see emotion trends and radio messages. Hover over points to view message details.

Future Enhancements:
1. Add multiple races for further analysis
2. Complete data collection for all drivers
3. Improve visual styling and layout with Streamlit components
4. Add leaderboards or rankings based on average emotions and compare to final race positions