import streamlit as st
from mychemtools import anti_checker, intro, reference

st.set_page_config(page_title="Chemical Analysis App", page_icon="#")

# create tabs
tab1, tab2, tab3 = st.tabs(["Introduction", "Anti-Checker", "References"])

with tab1:
    intro.intro_page()

with tab2:
    anti_checker.anti_checker_page()

with tab3:
    reference.reference_page()
