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
    page_0()
elif step == 1:
    page_1()
elif step == 2:
    page_2()
