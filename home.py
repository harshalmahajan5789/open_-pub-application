import streamlit as st
import numpy as numpy
import pandas as pd
from PIL import Image
from matplotlib import image
import os

st.title('Welcome to Open Pub Application 🍻')

#Background Image
img = '''
<style>
.stApp {
background-image: url("https://wallpapercave.com/w/wp10307759.jpg");
background-size: cover;
background-position: top center;
background-repeat: no-repeat;
background-attachment: local;
background-blur;
}
</style>
'''
st.markdown(img, unsafe_allow_html=True)

#Adding image
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
dir_of_interest = os.path.join(FILE_DIR, "resources")
IMAGE_PATH = os.path.join(dir_of_interest, "images")
IMAGE_PATH1 = os.path.join(IMAGE_PATH, "pubpic.jpg")
DATA_PATH1 = os.path.join(dir_of_interest, "open_pubs_updated.csv")

img = image.imread(IMAGE_PATH1)
st.image(img)

st.subheader('Find the Basic information of the pub dataset')


df = pd.read_csv(DATA_PATH1)

choice = st.selectbox('',('Total pubs in UK','unique Postal Code','unique local authority'))

if choice=='Total pubs in UK':
    st.markdown(f'There  are  **{df.shape[0]}**  Pubs  in  **United Kingdom**')

elif choice=='unique Postal Code':
     st.text(f'Total no of Postal Code is {len(df.postcode.unique())} in UK')


elif choice=='unique local authority':
    st.text(f'Total no of pub local authority is {len(df.local_authority.unique())} in UK')


elif choice=='Statistics information':
     st.dataframe(df.describe())

st.text('')
st.text('')

st.subheader('Find the Statistics information of the pub dataset')

stat = st.button('Statistics')
if stat==True:
    st.dataframe(df.describe())
else:
    st.text('')


#subheader
st.write('By Harshal Mahajan')