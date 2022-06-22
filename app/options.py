import streamlit as st
from viewer import render


def options(model_folder):

    design_options = {}

    for count, file_path in enumerate(model_folder.iterdir()):
        if not file_path.stem == 'gridbased':
            design_options[count] = file_path

    st.write(design_options)

    option = st.radio('Select design option', list(design_options.keys()))

    render(design_options[option], key='options')

    return design_options
