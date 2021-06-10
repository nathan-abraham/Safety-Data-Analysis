import pandas as pd # Reading csv files
import seaborn as sns # Graphing
import matplotlib.pyplot as plt # Graphing
import numpy as np # Math

air_df = pd.read_csv("datasets/air_quality_index_india.csv") # Read air data
air_df = air_df.drop(["COUNTRY"], axis=1) # Drop "Country" column since all data is from India
air_df.head() # Examine the first 5 entries of the dataframe

# Convert cities to numbers
cities = air_df["CITY"].unique()
cities_dict = {cities[i]:i for i in range(len(cities))} 
print(cities_dict)
air_df["CITY"] = air_df["CITY"].replace(cities_dict)
air_df.head()
