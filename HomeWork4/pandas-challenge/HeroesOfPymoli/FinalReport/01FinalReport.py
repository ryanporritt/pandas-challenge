#assignment4_option1

# Player Count

import pandas as pd

# Load in file
csvpath = "../Resources/02-Homework_04-Pandas_Instructions_HeroesOfPymoli_Resources_purchase_data"

# Read and display the CSV with Pandas
purchase_data_pd = pd.read_csv(csvpath)
purchase_data_pd.head()