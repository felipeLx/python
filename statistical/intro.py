"""
statistical to exploratory Data Analysis
"""
import pandas as pd
import matplotlib.pyplot as plt

df_swing = pd.DataFrame({
    "state": ["PA", "PA","PA","PA","PA","PA","PA","PA","OH"],
    "country": ["Erie", "Bradford", "Tioga", "McKean", "Potter", "Wayne", "Susquehanna", "Warren", "Ashtabula"],
    "dem_share": [60.08, 40.64, 36.07, 60.08, 40.64, 36.07, 60.08, 40.64, 36.07]
})

df_swing[['state', 'country', 'dem_share']]
_ = plt.hist(df_swing['dem_share'])
_ = plt.xlabel('percent of vote Obama')
_ = plt.ylabel('number of countries')
plt.show()