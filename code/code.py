import pandas as pd
import numpy as np

# Load data
data = pd.read_excel('./data/data.xlsx')

age = pd.read_excel('./data/age.xlsx')
age.index = np.arange(1, len(age)+1)

edu = pd.read_excel('./data/education.xlsx')
edu.index = np.arange(1, len(edu)+1)

prof = pd.read_excel('./data/profession.xlsx')
prof.index = np.arange(1, len(prof)+1)

# Data dictionary
data_dict = dict(age.to_dict(), **edu.to_dict(), **prof.to_dict())

data.replace(data_dict, inplace=True)
print(data.head())