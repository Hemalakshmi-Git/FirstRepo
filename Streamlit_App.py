import streamlit
import pandas
streamlit.title('Quotes for the day')
streamlit.header('Quote1')
streamlit.text('Good things take time 💻')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
