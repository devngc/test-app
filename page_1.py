import streamlit as st
from pollination_streamlit_viewer import viewer
from pathlib import Path


def page_1(month):
    st.write(f'The month is {month}')

    st.write(st.session_state)

    df_vtkjs = Path('./assets/daylight_factor.vtkjs')
    st.write(df_vtkjs)
    viewer(key='df-page-0', content=df_vtkjs.read_bytes())
