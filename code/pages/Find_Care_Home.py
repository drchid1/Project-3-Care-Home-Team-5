import pandas as pd
import streamlit as st
from pathlib import Path
import googlemaps
from config import google_key

# Take in an input address
input_address = st.text_input('Please enter your address:', 'Enter your address here')

st.write(""" You live in """, input_address)

# Find the distance between the input address and the care homes

gmaps = googlemaps.Client(key=google_key)

ch_dist = gmaps.distance_matrix(input_address, 'Russells Hall Hospital, Pensnett Road, Dudley, DY1 2HQ', mode='driving')

st.write(ch_dist)