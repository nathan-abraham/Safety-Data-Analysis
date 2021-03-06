import pandas as pd # Reading csv files
import seaborn as sns # Graphing
import matplotlib.pyplot as plt # Graphing
import numpy as np # Math

heart_df = pd.read_csv("datasets/heart.csv") # Read heart data
o2_df = pd.read_csv("datasets/o2Saturation.csv") # Read oxygen saturation data
heart_df.describe()

# Removing outliers

from scipy.stats import zscore
heart_zscores = zscore(heart_df) # Zscore assigns a score in terms of standard deviation
abs_heart_zscores = np.abs(heart_zscores) # Get rid of negatives

# Filter out values who are more than 3 Standard deviations off from the mean
filtered_entries = (abs_heart_zscores < 3).all(axis=1) 
heart_df = heart_df[filtered_entries]
heart_df.describe()

# Visualization of age distribution
plt.figure(figsize=(12, 6))
sns.set_style("dark")
sns.countplot(x='age', data=heart_df)
plt.show()

# Clean o2 data
o2_zscores = zscore(o2_df) # Zscore assigns a score in terms of standard deviation
abs_o2_zscores = np.abs(o2_zscores) # Get rid of negatives

# Filter out values who are more than 3 Standard deviations off from the mean
filtered_entries = (abs_o2_zscores < 3).all(axis=1) 
o2_df = o2_df[filtered_entries]
o2_df.describe()

# Plotting oxygen saturation distribution
plt.figure(figsize=(10, 5))
sns.set_style("dark")
sns.histplot(data=o2_df).set(xlabel="Oxygen Saturation")
plt.show()

# Plotting gender distribution
male_count = 0
female_count = 0

for value in heart_df["sex"]:
    if value == 0:
        female_count += 1
    else:
        male_count += 1

slices = [male_count, female_count]
labels = ["Male", "Female"]
plt.pie(slices, labels=labels, pctdistance=0.5)
plt.title("Gender distribution")
plt.show()