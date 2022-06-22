import streamlit as st
import extra_streamlit_components as stx
from model import model
from options import options
from submit import submit
from results import results
from pollination_streamlit_io import special


def main():

    host = special.get_host(key='get_host')
    if not host:
        host = 'web'
    st.session_state.host = host

    step = stx.stepper_bar(
        steps=['Getting started', 'options', 'Submit', 'Results'],
        is_vertical=False
    )

    if step == 0:
        model_folder = model()
        st.session_state.model_folder = model_folder
    elif step == 1:
        design_options = options(st.session_state.model_folder)
        st.session_state.design_options = design_options
    elif step == 2:
        status = submit()
        st.session_state.status = status
    elif step == 3:
        results(st.session_state.design_options, st.session_state.status)


if __name__ == '__main__':
    main()
