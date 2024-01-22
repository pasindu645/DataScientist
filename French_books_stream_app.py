import streamlit as st
import pandas as pd

# Load the CSV
df = pd.read_csv("french_books_reviews.csv")

# Create filter options
title_filter = st.selectbox("Filter by book_title", df["book_title"].unique())
author_filter = st.text_input("Filter by author")

# Apply filters
filtered_df = df.loc[(df["book_title"] == title_filter) & (df["author"].str.contains(author_filter))]

# Streamlit app
st.title('Book search')

# Display the filtered dataset
st.dataframe(filtered_df)

#when you run this app first run the steamApp.py Then enter the below command in the terminal.

#streamlit run .\streamApp.py 