import streamlit as st
from pollination_streamlit_viewer import viewer
from pathlib import Path


def model():
    model_folder = Path('./assets')
    model_path = model_folder.joinpath('gridbased.vtkjs')
    viewer(key='getting-started', content=model_path.read_bytes())

    return model_folder
