import streamlit as st
import pandas as pd
#import plotly.express as px
#import plotly.graph_objects as go
import matplotlib
from matplotlib import pyplot as plt
matplotlib.rcParams['figure.figsize'] = [30,10]
from PIL import Image
import seaborn as sns
st.set_page_config(page_title="Rory's Webpage", page_icon=":tada:", layout="wide")

df1 = pd.read_csv("https://raw.githubusercontent.com/rmldn/portfolio/main/movies.csv")
df = df1
df.head() # quick glimpse of data

df = df.fillna(0)

df['gross'] = df['gross'].astype('int64')
df['budget'] = df['budget'].astype('int64')
df.sort_values(by=['gross'], inplace=False, ascending=False)


df_num = df
for col in df_num.columns:
    if(df_num[col].dtype =='object'):
        df_num[col] = df_num[col].astype('category')
        df_num[col] = df_num[col].cat.codes


#with open("style.css") as f:
#    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
#----- Header Section
with st.container():
    st.subheader("")
    st.subheader("Rory Marrast, MSc, MRSC")
    htp1 = 'https://raw.github.com/rmldn/portfolio/blob/main/rm.JPG'
#    image = Image.open(htp1)
#    st.image(htp1,width=250)
    st.write("Data Analysis, Data Visualisation, Data Cleaning")
#    st.write("Using Python to solve your business challenges and generate digestable visualisations")

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand" href="https://youtube.com/dataprofessor" target="_blank">Chanin Nantasenamat</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#bioinformatics-tools">Bioinformatics Tools</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)





#------ Load assets
#img_aeroplane = Image.open("/Users/rory/PycharmProjects/website/Images/aeroplane.jpg")
#img_monkeypox = Image.open("/Users/rory/PycharmProjects/website/Images/monkeypox.jpg")
#img_pet = Image.open("/Users/rory/PycharmProjects/website/Images/pet.png")
# img_3 = Image.open("/Users/rory/PycharmProjects/website/Images/3.jpg")
# img_4 = Image.open("/Users/rory/PycharmProjects/website/Images/4.jpg")


#------ Summary

with st.container():
    st.write("-----")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Summary")
        #st.write("##")
        st.write( """I am here to use my extensive knowledge and experience of coding, data and visualisation to solve business challenges and
        bring value to your project.""")
        
#        st.write("""I consider myself precise, decisive and literal and i use these
#        attributes in line with the scientific mehtod to understand the challenge,
#        desired outcomes  and formulate a reliable and reproducable plan to tackle it.""")
        st.info('''
        - Experienced Analyst and Researcher with a passion to scientifically meet your data requirements. 
        - Applies stong background in scientific research to understand your needs devise a plan solve your problem.
        - Happy to discuss any data-based projects.
        ''')
#----- Projects

#### Current Projects


    with st.container():
        st.write("-----")
        st.write("")
        st.header("Current Projects")
        
# Project 0 - Correlation Heatmaps      
    with st.container():

#       st.write("-----")
        st.write("")
        st.subheader("Correlation Heat Maps")
        st.write("""Using data visualisations to reveal correlation strenth of variables in a large dataset""")
        
        st.dataframe(df1)
        fig = plt.figure()
    # st.write("-----")
    # st.subheader("The Heat Map")
        corr_mat = df_num.corr(method='pearson')
        sns.heatmap(corr_mat, annot=True)
        plt.title("Film Release Correlations - Heat Map")
        plt.xlabel("Film Release Metadata")
        plt.ylabel("Film Release Metadata")
        st.pyplot(fig)

    #Project 1 - Predicting International travellers from Changi Airport
    with st.container():

        st.write("-----")
        st.write("")
        st.header("Upcoming Projects")
        st.write("##")
        image_column, text_column = st.columns((1,2))
        with image_column:
#            st.image(img_aeroplane)
            with text_column:
                st.subheader("Predicting Changi Airport passenger numbers post COVID-19")
                st.write("""We set out to understand post-pandemic travel data.""")
                st.write("""Notable skills used: Python, Time Series, Forecasting, API""")


    #Project2 - Monkeypox dashboard

    with st.container():
        #st.write("")
        #st.header("My Projects")
        st.write("##")
        image_column, text_column = st.columns((1,2))
        with image_column:
#            st.image(img_monkeypox)
            with text_column:
                st.subheader("Interactive dashboard tracking global monekypox cases")
                st.write("""We are tracking the latest "public health emergency of international concern" """)
                st.write("Notable skills: API, Dashboards, Public Health Data")
    # Project 3 - Greater London Stolen Animals
    with st.container():
        st.write("-----")
        image_column, text_column = st.columns((1,2))
        with image_column:
#            st.image(img_pet)
            with text_column:
                st.subheader("Correlation study on stolen animals in London")
                st.write(""" Notable Skills: Correlation, Regression, Crime, Urban Data""")
    #
    # # Project 4 -?
    # with st.container():
    #     st.write("##")
    #     image_column, text_column = st.columns((1,2))
    #     with image_column:
    #         st.image(img_4)
    #         with text_column:
    #             st.subheader("")
    #             st.write("""""")

# ------ Skills list
