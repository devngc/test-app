import streamlit as st


def submit():

    return st.radio(
        'Set status', options=['incomplete', 'complete'], index=0)
