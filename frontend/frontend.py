import streamlit as st
import pandas as pd
import numpy as np
import requests

pd.set_option('display.max_colwidth', -1)   

st. set_page_config(layout="wide")
st.title('Job Finder')


def make_clickable(text, link):
    return f'<a target="_blank" href="{link}">{text}</a>'

# @st.cache(show_spinner=False)
def load_data(skill, loc, yoe):
    url = f'http://127.0.0.1:8080/?skill={skill}&location={loc}&yoe={yoe}'
    x = requests.get(url)
    data = pd.DataFrame(dict(x.json()))
    data = data.fillna('Not Available')
    data['Title'] = data.apply(lambda row: make_clickable(row.Title,row.link),axis=1)
    data = data[['Title','Company','CTC','Experience','Location','Description','Required Skills']]
    data = data.to_html(escape=False,)
    return data

col1, col2, col3, col4 = st.beta_columns([7,3,3,3])
with col1:
    skill = st.text_input('Skills',key='skills', help='Enter your skills')
with col2:
    loc = st.text_input('Location',key='loc', help='Enter location for job')
with col3:
    yoe = st.text_input('Years of experience',key='yoe', help='Enter your years of experience')
with col4:
    data = 'Please enter your skills, location and years of experience.'
    st.text('Submit')
    if st.button('Find Jobs',key='submit',help='Enter details and press the button.'):
        data_load_state = st.text('Finding Jobs. Required time may\nvary depending on internet speed.')
        # try:
        data = load_data(skill, loc, yoe)
        data_load_state.text('Jobs Found')
        # except Exception as e:
        #     data = f'Error: {e}<br>Please try again later.'
        #     data_load_state.text('Error!')
st.write(data,unsafe_allow_html=True)