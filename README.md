# Reviews Analysis
This repository contains code for extracting and analyzing customer product reviews data. In this example, we use Amazon product reviews for a television, which are extracted using RapidAPI. The final clean customer review data, which is suitable for analytics and product enhancement purposes, is stored in the file named "reviews_sentiment_clean_analysis.xlsx". The process of generating this file involves a four-step approach, and the corresponding Python files and Jupyter notebooks are provided in this repository. The filenames are numbered to indicate the order in which the code should be executed to achieve the final output.

1_rapid_api.py: This Python script is used to extract product reviews from Amazon using RapidAPI. The extracted reviews are raw data that require further processing.

2_extract_reviews.py: The output from RapidAPI is not in a tabular format. This Python script processes the raw data, extracts relevant data points, and organizes them into a tabular format. The resulting data is saved to a CSV file for further analysis.

3_openapi_call_scratch.ipynb: This Jupyter notebook contains code that iteratively calls GPT models for each review using the LangChain framework. The goal is to perform sentiment analysis on the reviews and obtain insights into customer opinions.

4_extract_sentiment.py: The output from the GPT models is in the form of nested dictionaries. This Python script extracts sentiment information from the nested dictionaries and organizes it back into a tabular format for easy analysis and interpretation.

Overall, this repository provides a comprehensive workflow for extracting, processing, analyzing, and interpreting customer product reviews data. The code is modular and can be adapted for similar use cases involving customer reviews analysis.




