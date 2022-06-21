import streamlit as st
import extra_streamlit_components as stx
from page_0 import page_0
from page_1 import page_1
from page_2 import page_2

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
elif step == 1:
    page_1(st.session_state.month)
elif step == 2:
    page_2(st.session_state.month)
