import streamlit as st
import pandas as pd

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
