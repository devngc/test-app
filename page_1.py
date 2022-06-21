import streamlit as st
from pollination_streamlit_viewer import viewer


def page_1(month, vtkjs):
    st.write(f'The month is {month}')

    st.write(st.session_state)

    viewer(key='df-page-0', content=vtkjs.read_bytes())
