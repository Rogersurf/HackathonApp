# Import necessary libraries
import streamlit as st
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

st.set_page_config(
    page_title="Group 5 Hackathon EDA Dashboard",
    page_icon="✅",
    layout="wide",
)

# Function to load the dataset
@st.cache_data  # Cache the function to enhance performance
def load_data():
    # Define the file path
    file_path = 'data with continents and without missing years.csv'
    
    # Load the CSV file into a pandas dataframe
    df = pd.read_csv(file_path)

    return df

# Load the data using the defined function
df = load_data()

# Set the app title and sidebar header
st.title("Student assigment - Renewable Energy: Let's Get Green 🌍♻️")
st.sidebar.header("Filters 📊")

st.markdown("""
            Sustainable energy analysis
""")
#with st.expander("📊 **Key Components of the Analysis**"):
 #                st.markdown("""
  #               - Years
 #                -
#"""
#)
                 

# Sidebar filter: Continent
continent = df['Continent'].unique().tolist()
selected_continent = st.sidebar.multiselect("Select Continent 🌍", continent, default=continent)
if not selected_continent:
    st.warning("Please select a department from the sidebar ⚠️")
    st.stop()
filtered_df = df[df['Continent'].isin(selected_continent)]

# Sidebar slider filter: Year
min_year = int(df['Year'].min())
max_year = int(df['Year'].max())
income_range = st.sidebar.slider("Select Yearly Range 📆", min_year, max_year, (min_year, max_year))
filtered_df = filtered_df[(filtered_df['Year'] >= income_range[0]) & (filtered_df['Year'] <= income_range[1])]

# Displaying the Analysis header
st.header("Analysis 📊")

# Dropdown to select the type of visualization
visualization_option = st.selectbox(
    "Select Visualization 🎨", 
    ["Box plot of Wordwide Renewable Electricity Generating Capacity Per Capity By Year",
    "Heatmap of Average Access to Clean Cooking Fuels by Continent and Year", 
    "Are renewables for the rich? (Scatterplot for each individual country)",
    "Scatterplot of GDP Growth vs. share of renewable energy by Continent"])

# Visualizations based on user selection
if visualization_option == "Box plot of Wordwide Renewable Electricity Generating Capacity Per Capity By Year":
# Boxplot for renewable electricity
# Display the average values
    barchart_data_pivot = filtered_df.pivot_table(index='Continent', columns='Year', values='Renewable-electricity-generating-capacity-per-capita')
# Create a barchart
    plt.figure(figsize=(12,6))
    sns.set_style("whitegrid")
    sns.catplot(data=barchart_data_pivot, kind="box")
# Customize the chart
    plt.title('Box plot of Wordwide Renewable Electricity Generating Capacity Per Capity By Year')
    plt.xlabel('Year')
    plt.ylabel('Renewable Electricity Generating')
    plt.xticks(rotation=45)

    plt.tight_layout()
    st.pyplot(plt)

elif visualization_option == "Heatmap of Average Access to Clean Cooking Fuels by Continent and Year":
    # Display the average values
    heatmap_data_pivot = filtered_df.pivot_table(index='Continent', columns='Year', values='Access to clean fuels for cooking')
    # Create a heatmap
    plt.figure(figsize=(10, 6))
    sns.set_style("whitegrid")
    sns.heatmap(data=heatmap_data_pivot, annot=True, cmap="YlGnBu")
    # Customize the chart
    plt.title('Heatmap of Average Access to Clean Cooking Fuels by Continent and Year')
    plt.xlabel('Year')
    plt.ylabel('Continent')

    plt.tight_layout()
    st.pyplot(plt)

elif visualization_option == "Are renewables for the rich? (Scatterplot for each individual country)":
    chart = alt.Chart(filtered_df).mark_point(filled=True).encode(
        alt.X('gdp_per_capita'),
        alt.Y('Renewables (% equivalent primary energy)'),
        alt.Size('Value_co2_emissions_kt_by_country', scale=alt.Scale(range=[100,500])),
        alt.Color('Continent'),
        alt.OpacityValue(0.7),
        alt.Tooltip('Country'))

    
    st.altair_chart(chart, use_container_width=True)

elif visualization_option == "Scatterplot of GDP Growth vs. share of renewable energy by Continent":
    # I remove all the NaN's from gdp growth and renewable energy shar
    df1 = filtered_df[filtered_df["gdp_growth"].isna() == False]
    df2 = df1[df1["Renewable energy share in the total final energy consumption (%)"].isna() == False]

    mean_df = filtered_df.groupby('Country')['gdp_growth','Renewable energy share in the total final energy consumption (%)'].mean().reset_index()

    merged_df = mean_df.merge(filtered_df[['Country', 'Continent',]], on='Country', how='left')

    plt.figure(figsize=(10, 6))
    sns.relplot(data=merged_df,
            x="gdp_growth",
            y="Renewable energy share in the total final energy consumption (%)",
            kind="scatter",
            hue="Continent",)
    plt.xlabel('average gdp growth')
    plt.ylabel('Share of renewable energy')
    plt.title('Scatterplot of GDP Growth vs. share of renewable energy by Continent')
    
    plt.tight_layout()
    st.pyplot(plt)

# Display dataset overview
st.header("Dataset Overview")
st.dataframe(df.describe())

# Insights from Visualization Section Expander
with st.expander("Insights from Visualization 🧠"):
    st.markdown("""
    1. **Age Groups & Attrition** - The 'Attrition by Age Group' plot showcases which age brackets face higher attrition.
    2. **Home Distance's Impact** - The 'KDE Plot: Distance from Home by Attrition' visualizes if being farther away influences leaving tendencies.
    3. **Roles & Attrition** - 'Attrition by Job Role' reveals which roles might be more attrition-prone.
    4. **Gender & Attrition** - The pie chart for 'Attrition Distribution by Gender' provides insights into any gender-based patterns.
    5. **Earnings Patterns** - 'MonthlyRate and DailyRate by JobLevel' boxplots display the compensation distribution across job levels.
    """)