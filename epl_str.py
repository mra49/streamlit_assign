import streamlit as st
import pandas as pd 
import plotly.express as px 
from PIL import Image

df = pd.read_csv("epldata_final.csv")

# Page title 
def home(df):
    st.title("EPL Transfer Market")
    # Image
    st.image("fpl.png")
    # Subheader under image just by code sequence
    st.subheader("Showcasing the Data")
    # Showcasing the data only first 23 rows
    st.write(df.head(23))

# # Title for 1st graph
# def Value_Age(df):
#     st.subheader("Market Value Relative to Age")
#     Fig_1 = px.scatter(df, x="age", y="market_value", size="fpl_points", hover_name="name", color="club")
#     st.plotly_chart(Fig_1)

# Title for 1st graph
def Value_Age(df):
    st.subheader("Market Value Relative to Age")
    
    # Explanation for legend interactions
    st.write("Double-click on legend items to choose/un-choose teams.")
    
    Fig_1 = px.scatter(df, x="age", y="market_value", size="fpl_points", hover_name="name", color="club")
    st.plotly_chart(Fig_1)


# Title for second graph
def Position_Age(df):
    st.subheader("Positions For Every Age")
    Fig_2 = px.scatter(df, x="age", y="position")
    # Allow the user to select a plot color
    col = st.color_picker("Select a plot color")
    # Set the plot color
    Fig_2.update_traces(marker=dict(color=col))
    st.plotly_chart(Fig_2)

# Third graph
def Value_Position(df):
    st.subheader("Market Value According to Positions")
    x_axis = st.selectbox("Select X-axis Value", options=df.columns)
    y_axis = st.selectbox("Select Y-axis Value", options=df.columns)
    plot = px.scatter(df, x=x_axis, y=y_axis)
    st.plotly_chart(plot)

# Add a tab for main findings
def main_findings(df):
    st.subheader("Main Findings")
    # Add your main findings here
    finding2 = '''Finding 1: If players want to increase there career span at the top level,
             they have to adapt their style of play to occupy more defensive role which can be seen from the second scatter plot.'''
    finding1 = '''Finding 2: The best time to sell players is when they are approaching the 28 years mark since this 
    is where their prices soar, the most valuable players aren't the ones that are too young, but the ones who have matured 
    and still are performing at their best (check 1st visual )'''    
    st.write(finding1)
    st.write(finding2)
    
    # You can add more findings as needed

options = st.sidebar.radio('Pages', options=["Home", "Value to Age", "Positions to Age", "Value to Position", "Main Findings"])

if options == "Home":
    home(df)
elif options == "Value to Age":
    Value_Age(df)
elif options == "Positions to Age":
    Position_Age(df)
elif options == "Value to Position":
    Value_Position(df)
else:
    main_findings(df)
