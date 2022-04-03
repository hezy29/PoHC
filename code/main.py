import pandas as pd
import numpy as np
from semopy import Model
from semopy import semplot
import desc
import pingouin as pg
from factor_analyzer.factor_analyzer import calculate_kmo, calculate_bartlett_sphericity

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

# Reliability
cronbach_alpha_all, cronbach_alpha_each = pg.cronbach_alpha(
    data=data[data.columns[10:]])
reliability = cronbach_alpha_all

# Validity
kmo_vars, kmo_model = calculate_kmo(data[data.columns[10:]])
chi2, p = calculate_bartlett_sphericity(data[data.columns[10:]])
validity = [kmo_model, chi2]

# Model
desc_1 = desc.mod1
mod_1 = Model(description=desc_1)
mod_1.fit(data)

# SEM plot
pic_1 = semplot(mod_1, "./PoHC/picture/mod_1.svg")
