import streamlit as st
import pandas as pd 
import plotly.express as px 
from PIL import Image

df = pd.read_csv("epldata_final.csv")
#page title 
def home(df):
    st.title("EPL Transfer Market")
#image
    st.image("fpl.png")
#subheader under image just by code sequence
    st.subheader("showcasing the Data")
#showcasing the data only first 23 rows
    st.write(df.head(23))

#title for 1st graph
def Value_Age(df):
    st.subheader("Market Value Relative to Age")
    Fig_1 = px.scatter(df,x = "age", y = "market_value", size = "fpl_points", hover_name = "name", color = "club")
    st.plotly_chart(Fig_1)

#title for second graph
def Position_Age(df):
    st.subheader("Positions For Every Age")
    Fig_2 = px.scatter(df, x = "age", y = "position")
    col = st.color_picker("select a plot color")
    st.plotly_chart(Fig_2)

#third graph
def Value_Position(df):
    st.subheader("Market Value According to Positions")
    x_axis = st.selectbox("Select X-axis Value", options = df.columns)
    y_axis = st.selectbox("Select Y-axis Value", options = df.columns)
    plot = px.scatter(df,x = x_axis, y= y_axis)
    #Fig_3 = px.bar(df, x = "position", y = "market_value")
    st.plotly_chart(plot)

options = st.sidebar.radio('Pages', options=["home", "Value to Age", "Positions to Age", "value to position" ])


if options == "home":
    home(df)
elif options == "Value to Age":
    Value_Age(df)
elif options == "Positions to Age":
    Position_Age(df)
else: 
    Value_Position(df)

