import streamlit as st


def page_0():
    month = st.text_input('enter the month')

    st.write(month)
    st.session_state.month = month
