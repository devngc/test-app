import streamlit as st
from pollination_streamlit_viewer import viewer


def page_2(vtkjs_path):
    st.write(vtkjs_path.stem)
    st.write(st.session_state)

    with st.form("my_form"):
        name = st.text_input('month name')

        submitted = st.form_submit_button("Submit")
        if submitted:
            if name == vtkjs_path.stem.split('_')[-1]:
                viewer(key='df-page-2', content=vtkjs_path.read_bytes())
