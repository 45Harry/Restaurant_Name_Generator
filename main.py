import streamlit as st

#from Restaurant_Name_Generator.langchain_helper import generate_restaurant_name_and_fooditems
from langchain_helper import generate_restaurant_name_and_fooditems

st.title("Resturant Name Generator")

cuisine = st.sidebar.selectbox('Pick a Cuisine',("Nepali","Maithli","Indian","French","American","Italian"))


if cuisine:
    response = generate_restaurant_name_and_fooditems(cuisine)
    st.header(response['restaurant_name'].strip())
    menu_items = response['menu_items'].strip().split(',')
    for item in menu_items:
        st.write('-',item)

