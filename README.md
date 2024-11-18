# Gen-AI Dashboard

## Project Summary

Gen-AI Dashboard is an AI-powered web application that utilizes the Google Gemini API to process data and extract relevant information from uploaded CSV files. The dashboard allows users to upload CSV files containing entities, perform web searches to gather relevant data, and use generative AI models to extract key information. 
## Features

- Upload CSV files with entities for processing.
- Customizable prompt template for querying data.
- Use of the Google Gemini API to generate meaningful content from search results.
- Filter extracted data based on search terms.
- Option to download processed results as a CSV file.
- Interactive user interface built with Streamlit.

## Setup Instructions

### Prerequisites

Before running the application, make sure you have the following installed:

- Python 3.9 or higher
- Streamlit
- Pandas
- Requests
- Google Gemini API (with API key)
  
### Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/Shvm17/gen-ai-dashboard.git
   ```

2. Navigate to the project directory:

   ```bash
   cd gen-ai-dashboard
   ```

3. Install the required dependencies::

   ```bash
   pip install -r requirements.txt
   ```
4. Create a .env file in the root directory with your API keys::

   ```bash
   GOOGLE_API="your-google-gemini-api-key"
   SERP_API = "your-serpapi-api-key"
   
   ```
   
5. Running the App: Start the Streamlit app.

  ```bash
  streamlit run app.py
  ``` 

## Usage Guide
- Upload your CSV file containing entities.
- Select the column that contains the entities.
- Provide a custom prompt template where {entity} is a placeholder for each entity in the selected column.
- View the extracted data, and optionally filter results based on specific search terms.
- Download the extracted data as a CSV file.

## Third-Party APIs & Tools Used
- Google Gemini API: A powerful generative AI tool for processing and extracting meaningful content from text snippets.
- SerpAPI: A search engine API used to gather search results from the web based on the entity and prompt provided.
- Streamlit: A Python library used to create interactive web applications for data processing and visualization.
- Pandas: A Python data analysis library for handling and processing data in CSV format.

## Acknowledgments
Special thanks to the contributors of the open-source libraries used in this project.


