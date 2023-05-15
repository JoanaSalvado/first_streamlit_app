import streamlit as st
import pandas as pd
import requests as rq
import snowflake.connector
from urllib.error import URLError

def get_fruityvice_data(fruit_choice):
  fruityvice_response = rq.get("https://fruityvice.com/api/fruit/" + fruit_choice)
  fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
  return fruityvice_normalized

def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("select * from fruit_load_list")
    return my_cur.fetchall()
  
def insert_row_snowflake(new_fruit):
  with my_cnx.cursor() as my_cur:
    my_cur.execute("insert into fruit_load_list values ('" + new_fruit + "')")
    return "Thanks for adding " + new_fruit
                  

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

try:
  fruit_choice = st.text_input('What fruit would you like information about?')
  if not fruit_choice:
     st.error('Please select a fruit to get information.')
  else:
    fruit_from_function = get_fruityvice_data(fruit_choice)
    st.dataframe(fruit_from_function)
except:
  st.error()

# Add a button to trigger the Fruit Load List
st.header('View Out Fruit List - Add Your Favorites!')
if st.button('Get Fruit List'):
  my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
  my_data_rows = get_fruit_load_list()
  my_cnx.close()
  st.dataframe(my_data_rows)

# Add a button to trigger the Snowflake aditions
if st.button('Add a Fruit to the list'):
  add_my_fruit = st.text_input('What fruit would you like to add?')
  st.text("insert into fruit_load_list values ('" + add_my_fruit + "')")
  #my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
  #fruit2add = insert_row_snowflake(add_my_fruit)
  #my_cnx.close()
  #st.text(fruit2add)

