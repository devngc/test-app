import streamlit as st


def page_2(month):
    st.write(f'The month is {month}')

    st.write(st.session_state)
