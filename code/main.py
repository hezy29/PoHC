import pandas as pd
import numpy as np
from semopy import Model
from semopy import semplot
import os
import desc

# Load data
data = pd.read_excel('./PoHC/data/data.xlsx')
data['time_used'] = data['time_used'].apply(lambda x: int(str(x)[:-1]))

age = pd.read_excel('./PoHC/data/age.xlsx')
age.index = np.arange(1, len(age)+1)

edu = pd.read_excel('./PoHC/data/education.xlsx')
edu.index = np.arange(1, len(edu)+1)

prof = pd.read_excel('./PoHC/data/profession.xlsx')
prof.index = np.arange(1, len(prof)+1)

# Data dictionary
data_dict = dict(age.to_dict(), **edu.to_dict(), **prof.to_dict())
data.replace(data_dict, inplace=True)

# Model
desc_1 = desc.mod1
mod_1 = Model(description=desc_1)
mod_1.fit(data)

# SEM plot
semplot(mod_1, "./PoHC/picture/mod_1.svg")
