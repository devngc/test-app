import streamlit as st


def page_1(month):
    st.write(f'The month is {month}')

    st.write(st.session_state)
