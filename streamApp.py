import streamlit as st
import pandas as pd

# Load the CSV
df = pd.read_csv("dev.csv")

# Create filter options
title_filter = st.selectbox("Filter by document_title", df["document_title"].unique())
question_text_filter = st.text_input("Filter by question_text")

# Apply filters
filtered_df = df.loc[(df["document_title"] == title_filter) & (df["question_text"].str.contains(question_text_filter))]

# Streamlit app
st.title('Q&A Session')

# Display the filtered dataset
st.dataframe(filtered_df)

#when you run this app first run the steamApp.py Then enter the below command in the terminal.

#streamlit run .\streamApp.py 