import pandas as pd
import streamlit as st
from pathlib import Path

# read the excel file
path_to_excel = Path(r'/Users/muraliveerabahu/Documents/03_Bootcamp/Challenges/Project-3-Care-Home-Team-5/data/nhomes_capacity.xlsx')
df = pd.read_excel(path_to_excel)

# show the dataframe on streamlit
st.dataframe(df, hide_index=True, height=700)