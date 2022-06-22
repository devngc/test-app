import streamlit as st
from pollination_streamlit_viewer import viewer


def options(model_folder):

    design_options = {}

    for count, file_path in enumerate(model_folder.iterdir()):
        if not file_path.stem == 'gridbased':
            design_options[count] = file_path

    st.write(design_options)
    return design_options
