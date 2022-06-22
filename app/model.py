import streamlit as st
import tempfile
from viewer import render
from pathlib import Path


def model():

    if 'temp_folder' not in st.session_state:
        st.session_state.temp_folder = Path(tempfile.mkdtemp())

    model_folder = Path('./assets')
    model_path = model_folder.joinpath('gridbased.hbjson')
    render(model_path)

    return model_folder
