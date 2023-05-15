import streamlit as st
import pandas as pd
import requests as rq
import snowflake.connector

st.title("My Mom's New Healthy Diner")
st.header('Breakfast Favorites')
st.markdown(':bowl_with_spoon: Omega 3 & Blueberry Oatmeal')
st.markdown(':green_salad: Kale, Spinach & Rocket Smoothie')
st.markdown(':chicken: Hard-Boiled Free-Range Egg')
st.markdown(':avocado::bread: Avocado Toast')
st.header(':banana::strawberry: Build Your Own Fruit Smoothie :kiwifruit::grapes:')

# Build the Fruit List for the smoothies, using s3 stored txt files
my_fruit_list = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')

# Use a interactive widget (Multi-select) that allows users to pick the fruits
## Ask user for the fruits - add a default set
fruits_selected = st.multiselect("Pick some fruits:", list(my_fruit_list.Fruit), ['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[my_fruit_list['Fruit'].isin(fruits_selected)]

## Display the table on the page
st.dataframe(fruits_to_show)

# Get Fruityvice API data
st.header('Fruityvice Fruit Advice!')

fruit_choice = st.text_input('What fruit would you like information about?', 'Kiwi')
st.write('The user entered', fruit_choice)

fruityvice_response = rq.get("https://fruityvice.com/api/fruit/" + fruit_choice)

# Make the Fruityvice data looking nice
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
st.dataframe(fruityvice_normalized)

my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
st.text("Hello from Snowflake:")
st.text(my_data_row)
