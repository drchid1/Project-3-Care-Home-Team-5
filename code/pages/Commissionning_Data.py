# %%
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
import pandas as pd

st.title('Care Home Data Analysis - for Commissioning')

# %%
# Load the CSV file into a DataFrame
file_path = "../data/CareHome-data.csv"
df = pd.read_csv(file_path)

# Clean the column names by removing newline characters
df.columns = df.columns.str.replace('\n', '')

df.head()

# %%
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
file_path = "../data/CareHome-data.csv"
df = pd.read_csv(file_path)

# Plot a histogram of the 'Capacity' column
plt.figure(figsize=(10, 6))
plt.hist(df['Capacity'], bins=30, edgecolor='black')  # Set edgecolor to 'black' or any color you prefer
plt.title('Distribution of Care Home Capacities')
plt.xlabel('Capacity')
plt.ylabel('Count of Care Homes')

# Save the plot as a PNG file
plt.savefig('../output/Capacity_histogram.png')

# Display the plot using Streamlit
st.pyplot(plt)

# %%
# Calculate the counts of each age range
age_range_counts = df['Age Range'].value_counts()

# Plot the bar chart
plt.figure(figsize=(10, 6))
plt.bar(age_range_counts.index, age_range_counts.values)
plt.title('Distribution of Age Ranges in Care Homes')
plt.xlabel('Age Range')
plt.ylabel('Count')
plt.xticks(rotation=45)

# Save the plot as a PNG file
plt.savefig('../output/Age_range_bar_chart.png')

# Show the plot
st.pyplot(plt)

# %%
# Plot 3: Ratings Distribution with different colors for each bar
rating_counts = df['Rating'].value_counts()
colors = ['skyblue', 'salmon', 'lightgreen', 'gold', 'orange']  # specify colors for each rating

plt.figure(figsize=(10, 6))
plt.bar(rating_counts.index, rating_counts.values, color=colors[:len(rating_counts)])
plt.title('Distribution of Care Home Ratings')
plt.xlabel('Rating')
plt.ylabel('Count')
plt.xticks(rotation=45)


# Save the plot as a PNG file
plt.savefig('../output/Rating_bar_chart.png')

# Show the plot
st.pyplot(plt)

# %%
import matplotlib.pyplot as plt

# Sample data
nursing_counts = df['Provide Nursing'].value_counts()

# Define the explode offset for each slice
explode = [0.1] * len(nursing_counts)

# Define four different colors
colors = ['#66b3ff', '#ff9999', '#99ff99', '#ffcc99']

# Create a pie chart
plt.figure(figsize=(10, 4))
wedges, texts, autotexts = plt.pie(nursing_counts, labels=None, startangle=90, autopct='', explode=explode, colors=colors)

# Create a custom legend outside the pie chart with autopct
plt.legend(wedges, [f'{category}: {count} ({angle:.1f}%)' for category, count, angle in zip(nursing_counts.index, nursing_counts, [(count / sum(nursing_counts)) * 100 for count in nursing_counts])], title="Categories", loc="right", bbox_to_anchor=(0.9, 0, 0.1, 1))

# Equal aspect ratio ensures that pie is drawn as a circle
plt.axis('equal')

plt.title('Proportion of Care Homes Providing Nursing Care')


# Save the plot as a PNG file
plt.savefig('../output/Nursing_pie_chart.png')

# Show the plot
st.pyplot(plt)


# %%



