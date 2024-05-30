# Project-3-Care-Home-Team-5

# Overview

We propose to create a free, open-source tool which can assist families in choosing a care home for their loved ones. There are commercially listed websites which can help in this process, but there can be bias in the information. Some care homes may be promoted on the search through paid advertising, and websites could omit care homes that are not willing to pay for advertising subscriptions. We have chosen the Dudley borough in the West Midlands as a test bed for our project. The Dudley Council has its own [website](https://adultsocialcaremarketplace.dudley.gov.uk/) hosting the search for local care homes in the area; however, this produces a list of care homes without visualisation of the care homes on a map.

We aimed to create an unbiased search tool for hospitals and families looking for care homes funded by the Dudley Borough Council. As we have taken the visualisation track for this project, we can display all the care homes on an interactive map close to the family home, which can better inform about travel. We will also be able to layer other features the care homes provide using other specialist services and options the care homes provide together with the Care Quality Commission Rating. We will also provide a statistical visualisation of the types of care homes, beds, and services the council has access to help future commissioning on the population's needs.      

## Team Members

- Najma Ali
- Abdifatah Daoud
- Eleanor Duplock
- Mohammad Liaqat
- Murali Veerabahu


## Visualisations

To fulfill our brief we created three different visualisations. 

One was created using matplotlib, and shows a range of commissionaing and care home information.

We used java leaflet to create an interactive map to show care home locations compared to each other and a user inputted home addresss.

Finally streamlit was used to create a table which returns a sorted list of care homes, based on input data. 


## Data

We used two main sources for the data for our project:

##### Dudley Borough Council Website
On the Dudley council website, we found an existing pdf file which listed the council funded care homes, basic contact information and a few further details.
to csv? to dataframe? clean data?...

##### Care Quality Commission (CQC) API
We then gathered extra data from the CQC API, using this we gathered information about the most recent CQC rating.

These sets of data were combined and cleaned. Age ranges were changed to minimum and maximum age categories, and postcodes were used to calculate latitude and longitude co-ordinates for plotting on the maps.

capacity data??


# Instructions on how to use and interact with the project

### API Keys
For security the API keys used to geocode and access CQC ratings have been hidden in seperate files. The Google API was used for geocoding. For the google API a google_key needs to be created and saved in the [code](code) directory.
```python
    google_key = "Insert your Google API Key"
```
For the interactive maps using Javascript again a google API key is necessay. Please create a config.js file in the [imap](code/imap) folder with the following code.
```javascript
    const config = {
        google_key : "Insert your Google API Key"
    };
```
For the CQC API an api_key.py file needs to be created in the [code](code) folder
```python
   subscription_key = "Insert your CQC API Key"
```

### Interactive map of Dudley Council Funded Care Homes
We have created an interactive map which shows the Dudley area. It has markers for all the council funded care homes. This is then filterable based on care needs, such as dementia, physical disability, mental health and more. Additionally, the user can add a marker of a home address to see which care homes are best located. Clicking on a marker then shows additional information; contact details, a latest CQC rating and the care needs the care home can support. 

### Streamlit App
The streamlit app opens to a page asking the user to enter a home address and age of the patient. Using the Google API it then returns a sorted dataframe of care homes, sorted by driving distance, with information such as a colour coded CQC rating and . This dataframe has the capacity to update according to live data, the number of beds avaliable sorted in a separate file lets user know current avaiblity.


# Ethical Considerations

All our data comes from publicly accessible sources, and contains no personal information, meaning there are few ethical concerns.
The Dudley council website and the CQC API states that all information is covered by the Open Government License which allows anyone to use and adapt information as long as the data is the latest version, and the sources are referenced as we do below.

The user is asked to input some personal data (e.g. an address) into the application, but this is not connected with any other personal information, and we do not collect or store this information in anyway.


# References

Dudley Borough Council website and PDF- https://www.dudley.gov.uk/residents/care-and-health/adult-health-social-care/housing-with-care-and-support/care-homes-residential-and-nursing/

Dudley List of Contracted Care Home Providers - https://www.dudley.gov.uk/media/ktclgusy/2023-24_approved_care_home_providers_within_the_dudley_borough_available_to_the_public.pdf

Care Quality Commission API - https://api-portal.service.cqc.org.uk/api-details#api=syndication&operation=get-changes-within-timeframe

matplotlib - https://matplotlib.org

streamlit - https://streamlit.io

google maps api - https://developers.google.com/maps

geojson code - https://geojson.org/





