import streamlit as st
from viewer import render


def results(design_options, status):

    if status == 'complete':
        option = st.text_input('Option number', value='1')
        try:
            render(design_options[int(option)], key='results')
        except (ValueError, KeyError):
            st.error('Not a valid option number.')
            return
    else:
        st.write(f'Simulation is {status}.')
