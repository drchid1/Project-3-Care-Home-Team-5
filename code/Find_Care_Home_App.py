import pandas as pd
import streamlit as st
from pathlib import Path
import googlemaps
from config import google_key


# Take in an input address and age
st.set_page_config(layout="wide")
with st.form("my_form"):
    st.title('Find a Care Home funded by Dudley Council')
    st.write('This app will help you find a care home near you based on your input address and age.')

    input_address = st.text_input('Please enter your address:', 'Enter your address here')

    input_age = st.slider('Please enter age of person:', 18, 120, 65)    

    submitted = st.form_submit_button(label='Submit')

    if submitted:
        # Read the CSV file
        path_to_csv = Path.cwd() / '..' / 'data' / 'CareHome-data.csv'
        df = pd.read_csv(path_to_csv)

        path_to_csv_capacity = Path.cwd() / '..' / 'data' / 'nhomes_capacity.xlsx'
        df_capacity = pd.read_excel(path_to_csv_capacity)

        # Create a new dataframe for distance
        df_dist = pd.DataFrame()
        df_dist_disp = pd.DataFrame()

        # Find the distance between the input address and the care homes

        # Copying columns from the original dataframe
        df_dist['Care_Home'] = df['Care Home Name']
        df_dist['Address'] = df['Name & Address']
        df_dist['CQC Rating'] = df['Rating']

        # Create a googlemaps client
        gmaps = googlemaps.Client(key=google_key)

        # Loop through the dataframe and find the distance
        for i in range(len(df_dist)):
            ch_dist = gmaps.distance_matrix(input_address, df_dist.loc[i,'Address'], mode='driving')
            df_dist.loc[i, 'Driving_Distance_Num'] = ch_dist['rows'][0]['elements'][0]['distance']['value']
            df_dist.loc[i, 'Driving_Distance'] = ch_dist['rows'][0]['elements'][0]['distance']['text']

            # Sort acending order df_dist by driving distance
            df_dist_disp = df_dist.sort_values(by='Driving_Distance_Num', ascending=True)

            df_dist_disp['Capacity'] = df_capacity['available_beds']
            # Splitting the Age Range column into 'Min Age' and 'Max Age'
            df_dist_disp['minAge'] = df['Age Range'].str.extract('(\d{2})')
            df_dist_disp['maxAge'] = df['Age Range'].str.extract('-(\d{2})')

            # Fill NaN values with 0
            df_dist_disp['minAge'] = df_dist_disp['minAge'].fillna(0)
            df_dist_disp['maxAge'] = df_dist_disp['maxAge'].fillna(0)

            # Change the data type of 'minAge' and 'maxAge' to integer
            df_dist_disp['minAge'] = df_dist_disp['minAge'].astype(int)
            df_dist_disp['maxAge'] = df_dist_disp['maxAge'].astype(int)

            # Filter if input age is >= minAge
            df_dist_disp = df_dist_disp[(df_dist_disp['minAge'] <= input_age)]

            # Filter if input age is <= maxAge only if maxAge is not 0
            df_dist_disp = df_dist_disp[(df_dist_disp['maxAge'] == 0) | (df_dist_disp['maxAge'] >= input_age)]

            # Filter if capacity is greater than 0
            df_dist_disp = df_dist_disp[(df_dist_disp['Capacity'] > 0)]

            # Drop the 'Driving_Distance_Num', 'minAge' and 'maxAge' columns
            df_dist_disp = df_dist_disp.drop(columns=['Driving_Distance_Num', 'minAge', 'maxAge'])

        


        # Apply the color_rating function to the 'Rating' column
        df_dist_disp = df_dist_disp.style \
         .applymap(lambda x: 'color: green' if 'Outstanding' in x else '', subset=['CQC Rating']) \
         .applymap(lambda x: 'color: green' if 'Good' in x else '', subset=['CQC Rating']) \
         .applymap(lambda x: 'color: orange' if 'Requires improvement' in x else '', subset=['CQC Rating']) \
         .applymap(lambda x: 'color: red' if 'Inadequate' in x else '', subset=['CQC Rating'])


        # Display the dataframe in Streamlit
        st.dataframe(df_dist_disp, hide_index=True, height=700)
