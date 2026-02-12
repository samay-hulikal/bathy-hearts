import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# Path to the directory containing the heart rate data
data_dir = Path("/home/samay/Desktop/Samay/Collective Behavior/Deep sea data/Heart/smoothed_highfreq_for_orit")

# Creating a list of .csv files in the directory
heart_csv_files = sorted([f for f in data_dir.glob("*.csv") if not f.name.startswith(".")]) # List comprehension necessary to avoid strange ._ORIT_ files
print(f"Found {len(heart_csv_files)} files")

# Load the file to see what's going on
df = pd.read_csv(heart_csv_files[0]) # This "reads" the .csv file and creates a DataFrame (pandas' main data structure)
print(type(df))
print(df.head()) # Shows the first 5 rows of the DataFrame
print(df.columns.tolist()) # Creates a list of column names as a python list
