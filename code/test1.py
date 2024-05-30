import streamlit as st
import pandas as pd
from pathlib import Path

# import csv file

path_to_csv = Path.cwd() / '..' / 'data' / 'CareHome-data.csv'
df = pd.read_csv(path_to_csv)

df = df.style \
    .applymap(lambda x: 'color: green' if 'Outstanding' in x else '', subset=['Rating']) \
    .applymap(lambda x: 'color: green' if 'Good' in x else '', subset=['Rating']) \
    .applymap(lambda x: 'color: orange' if 'Requires improvement' in x else '', subset=['Rating']) \
    .applymap(lambda x: 'color: red' if 'Inadequate' in x else '', subset=['Rating'])

st.dataframe(df, width=1000)