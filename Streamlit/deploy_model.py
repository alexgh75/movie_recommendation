###############################
# This program lets you       #
# - Create a dashboard        #
# - Evevry dashboard page is  #
# created in a separate file  #
###############################

# Python libraries
import streamlit as st
from PIL import Image

# User module files
from ml import ml

def main():

    #############
    # Main page #
    #############
    st.markdown(
    """
    <style>
    .main {
    background-color: #D3A8A8
    }

    .block-container {
    background-color: #D3A8A8;
    }
    .stHeader {
    background-color: #D3A8A8;
    }

    </style>
    """,
    unsafe_allow_html=True,
    )

    options = ['Home','Prediction','End']
    choice = st.sidebar.selectbox("Menu",options, key = '1')

    if ( choice == 'Home' ):
      st.title("Cinemate: Your Trusted Companion for Movie Suggestions")
      st.image('./images/movie.jpg')
      pass

    elif ( choice == 'Prediction' ):
      ml()

    else:
      st.title("We hope you enjoy the movie! Feel free to explore more recommendations")
      st.image('./images/thank.jpg')
      st.end()


main()
