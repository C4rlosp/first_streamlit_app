
import streamlit
#agregando titulo a la app
streamlit.title('My parents New healthy Diner')

#agregando el menu
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')
#agregando un encabezado
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
#importando una lista de frutas desde AWS S3
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

#permitiendo elegir de la lista las frutas que ellos quieran incluir
#streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
my_fruit_list = my_fruit_list.set_index('Fruit')

#display the table on the page

streamlit.dataframe(my_fruit_list)


