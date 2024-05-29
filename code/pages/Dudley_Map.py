import streamlit as st
import streamlit.components.v1 as components


st.write("""
## Dudley Council funded care homes
         """)

components.iframe("http://127.0.0.1:5500/code/map/index.html", height = 600, width = 700)