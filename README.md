# Python
Here I document a summary of my Python projects with a description of each project and what skills I showcase within the project. I have some experience with Data Engineering and have provided a few ETL/ELT projects.

## Data Cleaing/Analysis/ML
| Project Link | Area | Project Description | Libraries |    
|---|---|---|---|
| ⚕️ [COVID-19 Dashboard](https://github.com/bdavidson16/Python/tree/main/CDC%3A%20COVID-19%20Dashboard) | APIs, NoSQL connection | This is a dashboard that shows COVID-19 death information and updates on a weekly basis (every Thursday), provided by the CDC. | requests, pandas, matplotlib, dash, bson |  
| 🏠 [House Price Prediction](https://github.com/bdavidson16/Python/tree/main/House%20Price%20Prediction) | EDA, ML | Analysis on Housing prices and how their features affect these prices. Then, cleaning the data based on EDA for preparation for further analysis, hopefully machine learning. Also, this cleaned data could be visualized in Power BI/Tableau for a quick look at the data. |  pandas, matplotlib |  
| 🤕 [Treatments for COVID-19](https://github.com/bdavidson16/Python/tree/main/COVID19%20Treatments) | EDA | EDA of Zomato, an online food delivery and restaurant reservation service based in India. Python is used for this project to clean the data and then immediately create several different visuals, such as histograms and boxplots, to identify relationships amongst the data. | pandas, sqlalchemy, psycopg2, PostgreSQL |
| 🍟🍔 [Zomato](https://github.com/bdavidson16/Python/blob/main/Zomato.ipynb) | EDA, Visualization | EDA of Zomato, an online food delivery and restaurant reservation service based in India. Python is used for this project to clean the data and then immediately create several different visuals, such as histograms and boxplots, to identify relationships amongst the data. | pandas, numpy, matplotlib, seaborn |
***

## Data Engineering
| Project Link | Area | Project Description | Libraries |    
|---|---|---|---|
| ✈️ [Apache Airflow DAG](https://github.com/bdavidson16/Python/blob/main/ETL%20Projects/ETL_toll_data.py) |  ETL |In this assignment, I developed an Apache Airflow DAG that extracts data from a *CSV*, a *TSV*, and a *fixed-width* file, transformS the data, and then loads the new data into the staging area (in this case it was a local directory). | Python, Airflow | 
| 💰 [ETL for Currency Exchange Rates](https://github.com/bdavidson16/Python/blob/main/ETL%20Projects/Final_Project_for_Py_Google_Analytics_Cert.ipynb) | Web-scraping, ETL in Python | I extracted data by scraping a wikipedia page with information on banks around the world and loading it into a pandas' dataframe. I also loaded a separate CSV file with information used to calculate the exchange_rate. Then I cleaned, manipulated and exported the data it into both a CSV file and SQLite database. |  BeautifulSoup, pandas, CSV, SQLite |
***
