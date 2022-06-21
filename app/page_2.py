import streamlit as st
from pollination_streamlit_viewer import viewer


def page_2(vtkjs_path):
    st.write(vtkjs_path.stem)
    st.write(st.session_state)

    viewer(key='df-page-2', content=vtkjs_path.read_bytes())
