import pandas as pd
import numpy as np
from semopy import Model, semplot, calc_stats
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

header = pd.read_excel('./PoHC/data/header.xlsx')

# Columns to inverse
inv_col = ['doubt_hc', 'govern_viola_priv', 'unnece',
           'sec_hand_used', 'viola_priv', 'diss_manda_hc', 'dislike_hc']
data[inv_col] = data[inv_col].apply(lambda x: 5-x)


# Data dictionary
data.columns = header.loc[1].values
data_dict = dict(age.to_dict(), **edu.to_dict(), **prof.to_dict())
data.replace(data_dict, inplace=True)
data.drop(columns=['anti_robot'], inplace=True)

# Reliability
cronbach_alpha_all, cronbach_alpha_each = pg.cronbach_alpha(
    data=data[data.columns[10:]])
reliability = cronbach_alpha_all

# Validity
kmo_vars, kmo_model = calculate_kmo(data[data.columns[10:]])
chi2, p = calculate_bartlett_sphericity(data[data.columns[10:]])
validity = [kmo_model, chi2]

# Model
desc_basic = desc.mod_basic_chi
mod_basic = Model(description=desc_basic)
mod_basic.fit(data)

desc_fixed = desc.mod_fixed_chi
mod_fixed = Model(description=desc_fixed)
mod_fixed.fit(data)

# Fit indices
stats = calc_stats(model=mod_fixed)
stats.T.to_excel("./PoHC/out/fit_indices.xlsx")

# SEM plot
mod_basic_no_params = semplot(
    mod_basic, "./PoHC/picture/mod_basic_no_params.pdf", plot_ests=False)
mod_basic_with_params = semplot(
    mod_basic, "./PoHC/picture/mod_basic_with_params.pdf", plot_ests=True, std_ests=True)
