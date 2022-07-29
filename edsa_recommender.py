"""

    Streamlit webserver-based Recommender Engine.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within the root of this repository for guidance on how to use
    this script correctly.

    NB: !! Do not remove/modify the code delimited by dashes !!

    This application is intended to be partly marked in an automated manner.
    Altering delimited code may result in a mark of 0.
    ---------------------------------------------------------------------

    Description: This file is used to launch a minimal streamlit web
	application. You are expected to extend certain aspects of this script
    and its dependencies as part of your predict project.

	For further help with the Streamlit framework, see:

	https://docs.streamlit.io/en/latest/

"""
# Streamlit dependencies
import streamlit as st
import streamlit.components.v1 as components


# Data handling dependencies
import pandas as pd
import numpy as np

import requests
from PIL import Image
import codecs

# Custom Libraries
from utils.data_loader import load_movie_titles
from utils.load import local_css
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model

#visualizations
import base64
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import RendererAgg
from matplotlib.figure import Figure
import seaborn as sns
from wordcloud import WordCloud
import sweetviz as sv
_lock = RendererAgg.lock

# Data Loading
title_list = load_movie_titles('resources/data/movies.csv')
movies_df = pd.read_csv('./resources/data/movies.csv')

# App declaration
def main():
    
    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    page_options = ["Recommender System","Solution Overview", "About us", "Contact us"]

    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------
    page_selection = st.sidebar.selectbox("Choose Option", page_options)
    if page_selection == "Recommender System":
        # Header contents
        st.write('# Movie Recommender Engine')
        st.write('### EXPLORE Data Science Academy Unsupervised Predict')
        st.image('resources/imgs/Image_header.png',use_column_width=True)
        # Recommender System algorithm selection
        sys = st.radio("Select an algorithm",
                       ('Content Based Filtering',
                        'Collaborative Based Filtering'))

        # User-based preferences
        st.write('### Enter Your Three Favorite Movies')
        movie_1 = st.selectbox('Fisrt Option',title_list[14930:15200])
        movie_2 = st.selectbox('Second Option',title_list[25055:25255])
        movie_3 = st.selectbox('Third Option',title_list[21100:21200])
        fav_movies = [movie_1,movie_2,movie_3]

        # Perform top-10 movie recommendation generation
        if sys == 'Content Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = content_model(movie_list=fav_movies,
                                                            top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


        if sys == 'Collaborative Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = collab_model(movie_list=fav_movies,
                                                           top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


    # -------------------------------------------------------------------

    # ------------- SAFE FOR ALTERING/EXTENSION -------------------
    if page_selection == "Solution Overview":
        st.title("Solution Overview")
        st.subheader("NFINATE CONSULTANT")
        st.write("Facebook, YouTube, LinkedIn are among the most used websites on the internet today that use recommender systems. Facebook suggests us to make more friends using the 'People You May Know' section. Similarly, LinkedIn recommends you connect with people you may know, and YouTube suggests relevant videos based on your previous browsing history. All of these are recommender systems in action.")
        st.write("While most of the people are aware of these features, only a few know that the algorithms used behind these features are known as 'Recommender Systems'. They 'recommend' personalised content based on user's past / current preference to improve the user experience. ")
        st.write("We were tasked with accurately predicting unseen movie ratings gathered from thousands of users based on their historic preferences. ")
        st.write("Broadly, there are two types of recommendation systems: Content-Based and Collaborative filtering based as mention. In the notebook, we observation algorithms of both content-based and collaborative filtering.")

        
    if page_selection == "About us":
        st.title("NFINATE CONSULTANT")
        st.subheader("Who are we?")
        st.write(
            "NFINATE CONSULTANT is a freelance tech startup specialised in Data Science, Machine Learning, Data Analysis, and Business Intelligence. ")
        st.write("Our team of expert scientists and researchers is dedicated to helping companies derive insightful information from existing data. By doing so Eagle Analytics hardwork is oriented in facilitating decision making as well prediction in business setting.")
        st.write("Our vision is to make the world a better place through hidden insight in data")
        st.subheader("Meet the team")
        # team members
        Oswald = Image.open('img/Oswald.png')
        Mune = Image.open('img/Mune.png')
        Abienwense = Image.open('img/Abienwese.png')
        Jan = Image.open('img/Jan.png')

        # Oswald
        col1, col2 = st.columns(2)
        with col1:
            st.image(Oswald)
        with col2:
            st.subheader("Oswald Cedric Syeni (CEO)") 
            st.write("Oswald has his PhD in Business Intellingence and over 15 years of experience running most successful businesses like Google, Microsoft, Oracle and Explore AI")       
            st.write(
                "With this blend of skills and experience the CEO and his team has helped over 250 startups improve their service")
        
        # Mune
        col1, col2 = st.columns(2)
        with col1:
            st.image(Mune)
        with col2:
            st.subheader("Mune Vani (Co-founder)")
            st.write(
                "Mune has a master in Project Management from Havard University and has applied his knowlege in numerous fortune Startup")
            st.write("During her 30 years of experience she has managed the development of well known and successfull products like Iphone 6, Iphone X, Iphone 11 Pro, and recently Samsung 22 before he moved to NFINITE CONSULTANTS ")

        # Abienwense
        col1, col2 = st.columns(2)
        with col1:
            st.image(Abienwense)
        with col2:
            st.subheader("Abienwense Head of R&D")
            st.write("Being a Master holder in Machine learning from the University of Michigan, Abienwense developed the machine learning algorithm for Tesla self driving and was the team lead for its implementation")
            st.write("She has also been CTO of numero organizations like Alibaba, Jumia, and Amazone where he has gained practinal knowledge that he put in use for the succcess of the startup")

        # Jan
        col1, col2 = st.columns(2)
        with col1:
            st.image(Jan)
        with col2:
            st.subheader("JAN LEGODI  (COO)")
            st.write(
                "He has her PhD in Business Administration from Polytechnique University in Canada and is dedicated in successfuly running Business.")
            st.write(
                "he spent the fifteen years of her successful career at Silicon Valley where he has helped the compamy inscrease its revenue by 80 percent")


    if page_selection == "Contact us":
        st.title("Contact us")
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Contact info")
            st.write("Cola Street, Near ATTC,")
            st.write("Adjacent Sociate Generale, Head Office,")
            st.write("Kokomlemle, P.O. Box AN0000, Accra")
            st.write("Telephone:+233 00 111 2222")
            st.write("WhatsApp:+234 210 12344 1390")
            st.write("Email: eagleanalytics@gmail.com")
            st.write("Website: eagleanalytics.com")
        with col2:
            st.subheader("Email Us")
            email = st.text_input("Enter your email")
            message = st.text_area("Enter your message")
            st.button("Send")

# Required to let Streamlit instantiate our web app.       
  
if __name__ == '__main__':
    main()
