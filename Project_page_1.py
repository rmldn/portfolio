#Changi airport passenger numbers forecast

# ------ Imports
import streamlit as st
from PIL import Image
import plotly.figure_factory as ff
import numpy as np
from pandas import to_datetime
from neuralprophet import NeuralProphet
import pickle
import csv
import pandas as pd
from matplotlib import pyplot as plt

### Data from sg.gov_time-series.py
df = pd.read_csv("/Users/rory/Documents/Coding/Python-testing-misc/sg.gov_air_pax_dep.csv")
hk = df[df['Country'] == 'Hong Kong']
hk.reset_index(drop=True, inplace=True)
print(hk)
hk['No of Pax'] = pd.to_numeric(hk['No of Pax'])
hk["Year"] = pd.to_datetime(hk["Year"])
hk.head()
hk['Date'] = hk['Year'].apply(lambda x: x.year)
# hk = hk[hk['Date']>=2015]
hk = hk[hk['Date'] <= 2020]
data = hk[['Year', 'No of Pax']]
data.dropna(inplace=True)  # Change applies to existing columns
data.columns = ['ds', 'y']  # Rename Year and No of Pax columns
data.reset_index()
data.head()
###
st.set_page_config(page_title="project_page_1", page_icon=":tada:", layout="wide")
###########




# Overview
with st.container():
    st.title("Predicting Changi Airport passenger numbers post COVID-19")

#Scientific method/plan
with st.container():
    st.write("-----")
    text_column_1, text_column_2, text_column_3 = st.columns((1,2,3))
# ------ Objective/Hypothesis
    with text_column_1:
        st.subheader("Hypothesis")
        st.write("Passenger numbers will ABC")
#------ Plan
    with text_column_2:
        st.subheader("Plan")
        st.write("gather data from sg.gov")
#------ Project Duration?
    with text_column_3:
        st.subheader("Project Duration?")
        st.write("one to two weeks")


#Results

#------ Graph/figure/dashboard
with st.container():
    st.write("-----")
    st.subheader("Results")
    st.write("Passenger numbers should seasonaly increase and...")

    # Add scatter data from sg.gov_time-series.py
    with open ("/Users/rory/PycharmProjects/DashPlotty/saved_model.pkl", "rb") as f:
        m = pickle.load(f)
    future = m.make_future_dataframe(data, n_historic_predictions=True, periods=30)
    forecast = m.predict(future)
    forecast.head()

    fig, ax = plt.subplots(figsize=(9, 6), linewidth=20)
    m.plot(forecast, xlabel="Years", ylabel="Passenger Numbers", ax=ax)
    ax.set_title("Changi Airport - International Passengers", fontsize=16, fontweight="bold")
    ax.plot(linewidth=1)
    plt.grid(False)
    plt.legend(["Last Forecast", "Actual Figures"])
    plt.show()
    st.pyplot(plt.show())
