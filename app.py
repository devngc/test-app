import streamlit as st
import extra_streamlit_components as stx
from page_0 import page_0
from page_1 import page_1
from page_2 import page_2
from pathlib import Path

step = stx.stepper_bar(
    steps=['page-1', 'page-2', 'page-3'],
    is_vertical=False
)


if step == 0:
    month = page_0()
    if 'month' not in st.session_state:
        st.session_state.month = month
    if month:
        st.session_state.month = month
    st.session_state.vtkjs = Path('./assets/daylight_factor.vtkjs')
elif step == 1:
    page_1(st.session_state.month, st.session_state.vtkjs)
elif step == 2:
    page_2(st.session_state.month)
