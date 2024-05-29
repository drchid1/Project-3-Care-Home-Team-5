import pandas as pd
import streamlit as st
from pathlib import Path

# read the excel file
path_to_excel = Path.cwd() / '..' / 'data' / 'nhomes_capacity.xlsx'
df = pd.read_excel(path_to_excel)

# Title and description
st.title('Care Home Capacity')
st.write('This page shows the capacity of care homes funded by Dudley Council.')

# show the dataframe on streamlit
st.dataframe(df, hide_index=True, height=700)