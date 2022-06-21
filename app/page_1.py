import streamlit as st
from pollination_streamlit_viewer import viewer


def page_1(month, vtkjs_folder):
    st.write(f'The month is {month}')

    st.write(st.session_state)

    vtkjs_path = vtkjs_folder.joinpath(f'daylight_factor_{month}.vtkjs')
    viewer(key='df-page-1', content=vtkjs_path.read_bytes())

    return vtkjs_path
