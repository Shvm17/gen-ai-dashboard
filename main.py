import pandas as pd
import streamlit as st
import requests
import os
import google.generativeai as genai  
from datetime import datetime
import time

# Configuring the Google Gemini API with your API key
genai.configure(api_key=os.getenv("GOOGLE_API"))

# Initialize the Gemini model
model = genai.GenerativeModel("gemini-pro")

# Here, this function will use the Gemini API for processing the data as per the user's query
def gemini_response(prompt):
    response = model.generate_content(prompt)
    return response.text.strip()

# This will Set up your Streamlit app
st.title("Gen-AI Dashboard")

# Custom Sidebar for Settings and other Options
st.sidebar.title("Settings")

uploaded_file = st.sidebar.file_uploader("Please Upload your CSV file", type=["csv"])

st.info("Upload a CSV file containing entities, select the column, and then provide a custom prompt to extract relevant data.")
extracted_data = []

# Now, Load the data and process if a file is uploaded.
extracted_data_df = pd.DataFrame()
if uploaded_file:
    with st.spinner("Processing your file..."):
        time.sleep(2)
        df = pd.read_csv(uploaded_file)
    
    st.write("Preview of Uploaded Data:")
    st.dataframe(df)

    # Let the user choose a column
    column = st.sidebar.selectbox("Select the main column for entities:", df.columns)
    st.sidebar.write(f"Selected column: {column}")

    #Take the user's custom prompt 
    prompt_template = st.sidebar.text_input("Enter your custom prompt (use {entity} as a placeholder):")
    
   

    # This Function will be used to perform a web search using a search API (SerpAPI)
    def perform_search(query):
        api_key = "fae6c4cb56997653757d8736b14003d0dab6f4871db66262adfe45a0c20dd26e"  # Replace with your actual SerpAPI key
        url = f"https://serpapi.com/search?q={query}&api_key={api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            st.error("Error in search API call.")
            return None

    if prompt_template:
        for entity in df[column]:
            query = prompt_template.format(entity=entity)
            search_results = perform_search(query)

            if search_results:
                snippet = search_results.get("organic_results", [{}])[0].get("snippet", "No snippet available")
                url = search_results.get("organic_results", [{}])[0].get("link", "No URL available")

                parsed_text = gemini_response(prompt_template.format(entity=entity))
                extracted_data.append({
                    "Entity": entity,
                    "Snippet": snippet,
                    "URL": url,
                    "Parsed Information": parsed_text
                })

        extracted_data_df = pd.DataFrame(extracted_data)
        st.write("Extracted Information:")
        st.dataframe(extracted_data_df)
        st.download_button("Download CSV", extracted_data_df.to_csv(index=False), "results.csv")

    

    search_term = st.text_input("Search in extracted data:")
    if search_term:
        filtered_data = extracted_data_df[extracted_data_df['Entity'].str.contains(search_term, case=False)]
        st.write(f"Filtered Results for: {search_term}")
        st.dataframe(filtered_data)

with st.expander("View Raw Data"):
    st.write(extracted_data)

st.markdown("""
<style>
.stButton>button {
    background-color: #4CAF50;
    color: white;
    font-size: 16px;
    border-radius: 5px;
}
</style>
""", unsafe_allow_html=True)
