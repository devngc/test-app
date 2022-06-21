import streamlit as st
from pollination_streamlit_viewer import viewer


@st.cache
def get_vtkjs_path(month, vtkjs_folder):
    return vtkjs_folder.joinpath(f'daylight-factor_{month}.vtkjs')


def page_1(month, vtkjs_folder):
    st.write(f'The month is {month}')

    st.write(st.session_state)

    vtkjs_path = get_vtkjs_path(month, vtkjs_folder)
    viewer(key='df-page-1', content=vtkjs_path.read_bytes())

    return vtkjs_path
