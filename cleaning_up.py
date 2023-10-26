# This is Data Cleaning with Pandas. We're selecting 12 columns out of 61:
# "AccMedianX", "AccMedianY", "AccMedianZ", "GyroMeanX", "GyroMeanY", "GyroMeanZ", 
# "GyroMedianX", "GyroMedianY", and "GyroMedianZ" 

import pandas as pd

input_filename = "features_14.csv"

# Read the csv file
total_data = pd.read_csv(input_filename)
# Displaying file information
# total_data.info()

# Select the 12 column names
columns_of_interest = ["AccMedianX", "AccMedianY", "AccMedianZ",
                       "GyroMeanX", "GyroMeanY", "GyroMeanZ",
                       "GyroMedianX", "GyroMedianY", "GyroMedianZ"]
filtered_data = total_data[columns_of_interest]

# Testing the filtered data for accuracy
# print(filtered_data)