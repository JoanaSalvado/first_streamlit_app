import streamlit as st
import pandas as pd

st.title("My Mom's New Healthy Diner")
st.header('Breakfast Favorites')
st.markdown(':bowl_with_spoon: Omega 3 & Blueberry Oatmeal')
st.markdown(':green_salad: Kale, Spinach & Rocket Smoothie')
st.markdown(':chicken: Hard-Boiled Free-Range Egg')
st.markdown(':avocado::bread: Avocado Toast')
st.header(':banana::strawberry: Build Your Own Fruit Smoothie :kiwifruit::grapes:')

my_fruit_list = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
st.dataframe(my_fruit_list)
