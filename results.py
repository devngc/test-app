import streamlit as st
from pollination_streamlit_viewer import viewer


def results(design_options, status):

    if status == 'complete':
        option_num = st.text_input('Option number', value='1')
        try:
            viewer(key='results', content=design_options[int(option_num)].read_bytes())
        except (ValueError, KeyError):
            st.error('Not a valid option number.')
            return
    else:
        st.write(f'Simulation is {status}.')
