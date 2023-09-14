# Import necessary libraries
import streamlit as st
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt
import seaborn as sns

# def main():
#     st.title("My First Streamlit App")

#     # Adding a text input widget
#     user_input = st.text_input("Enter your name", "Type Here...")

#     if st.button('Say Hello'):
#         st.write(f'Hello, {user_input}!')

# if __name__ == "__main__":
#     main()



# Function to load the dataset
@st.cache  # Cache the function to enhance performance
def load_data():
    # Define the file path
    file_path = ".\\data\\data with continents and without missing years.csv"
    
    # Load the CSV file into a pandas dataframe
    df = pd.read_csv(file_path)

    return df

# Load the data using the defined function
df = load_data()

# Set the app title and sidebar header
st.title("Student assigment - Renewable Energy lets gets green 🌍♻️")
st.sidebar.header("Filters 📊")

st.markdown("""
            Beginning with the significance of clean cooking fuels, which have a direct influence on public health and lower indoor air pollution, is a good place to start. Then, transition into the broader context of clean and renewable energy sources, highlighting the growth in renewable electricity generation and its share in total energy consumption.
Compare CO2 emissions amongst nations, paying particular attention to those that have made progress in adopting renewable energy.
Examine the economic aspect by showcasing GDP growth and GDP per capita trends in relation to clean energy development.
Narrate how countries have progressed in adopting clean energy sources, the challenges they face, and the potential economic and environmental benefits.This site is to showcase the currenct energy consumption
""")
with st.expander("📊 **Key Components of the Analysis**"):
                 st.markdown("""
A1. Access to Clean Cooking Fuels (% of Population): Start by addressing the percentage of the population with access to clean cooking fuels. This can be a critical factor for public health and the environment.

2. Renewable-Electricity-Generating-Capacity-Per-Capita: Explore the renewable electricity generation capacity per capita to highlight the transition toward cleaner energy sources.

3. Renewable Energy Share in Total Final Energy Consumption (%): Illustrate the share of renewable energy in the overall energy consumption, emphasizing the shift towards sustainability.

4. Electricity from Renewables (TWh): Highlight the absolute amount of electricity generated from renewable sources to showcase the impact of clean energy.

5. Value_CO2_Emissions_kt_by_Country: Show the CO2 emissions by country to provide context for the environmental impact.

6. Renewables (% Equivalent Primary Energy): Explore the percentage of renewables in the equivalent primary energy mix to emphasize the importance of clean energy sources.

7. GDP Growth and GDP per Capita: Examine the economic indicators like GDP growth and GDP per capita to understand how clean energy adoption relates to economic prosperity.

8. Access to Electricity (% of Population): Include access to electricity as a related factor, as it is often linked to energy development and clean energy adoption.

9. Latitude and Longitude: If there are geographic patterns in clean energy adoption, you can use latitude and longitude to create geographical visualizations.

10. Density (P/Km2) and Land Area (Km2): Consider including population density and land area to assess the impact of clean energy policies on densely populated areas or regions with significant land resources.
"""
)
                 

# Sidebar filter: Continent
continent = df['Continent'].unique().tolist()
selected_continent = st.sidebar.multiselect("Select Continent 🌍", continent, default=continent)
if not selected_continent:
    st.warning("Please select a department from the sidebar ⚠️")
    st.stop()
filtered_df = df[df['Continent'].isin(selected_continent)]


# Sidebar filter: Year
year = df['Year'].unique().tolist()
selected_year = st.sidebar.multiselect("Select Year", year, default=year)
if not selected_year:
    st.warning("Please select a year from the sidebar ⚠️")
    st.stop()
filtered_df = filtered_df[filtered_df['Year'].isin(selected_year)]

# Display dataset overview
st.header("Dataset Overview")
st.dataframe(df.describe())