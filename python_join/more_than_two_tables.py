# theoretical merge
grants_licenses = grants.merge(licenses, on="zip")
print(grants_licenses.loc[grants_licenses["business"] == "REGGIE'S BAR & GRILL", 
    ["grant", "company", "company", "account", "ward", "business"]])

# the licenses table will be matched to multiple businesses in the grants table with the same zip
# the output of the merge duplicates Reggie's bar for each matching zip in the grants table, which is not what we want

# best practice: merge two arguments
grants.merge(licenses, on=["address", "zip"])

# multiple tables
grants_licenses_ward = grants.merge(licenses, on=["address", "zip"]) \
    .merge(wards, on="ward", suffixes=("_bus", "_ward"))
grants_licenses_ward.head()

import matplotlib.pyplot as plt
grant_licenses_ward.groupby("ward").agg("sum").plot(kind="bar", y="grant")
plt.show()

# 3 tables
df1.merge(df2, on="col") \
    .merge(df3, on="col")

# 4 tables
df1.merge(df2, on="col") \
    .merge(df3, on="col") \
    .merge(df4, on="col")

ridership_cal = ridership.merge(cal, on=["year", "month", "day"])
ridership_cal_stations = ridership.merge(cal, on=['year','month','day']) \
            				.merge(stations, on="station_id")

# Create a filter to filter ridership_cal_stations
filter_criteria = ((ridership_cal_stations['month'] == 7) 
                   & (ridership_cal_stations['day_type'] == 'Weekday') 
                   & (ridership_cal_stations['station_name'] == 'Wilson'))

# Use .loc and the filter to select for rides
print(ridership_cal_stations.loc[filter_criteria, 'rides'].sum())

licenses_zip_ward = licenses.merge(zip_demo, on="zip") \
            			.merge(wards, on="ward")

# Print the results by alderman and show median income
print(licenses_zip_ward.groupby("alderman").agg({'income':'median'}))

# Merge land_use and census and merge result with licenses including suffixes
land_cen_lic = land_use.merge(census, on="ward") \
    .merge(licenses, on="ward", suffixes=["_cen", "_lic"])


# Group by ward, pop_2010, and vacant, then count the # of accounts
pop_vac_lic = land_cen_lic.groupby(["ward", "pop_2010", "vacant"], 
                                   as_index=False).agg({'account':'count'})

# Merge land_use and census and merge result with licenses including suffixes
land_cen_lic = land_use.merge(census, on='ward') \
                    .merge(licenses, on='ward', suffixes=('_cen','_lic'))

# Group by ward, pop_2010, and vacant, then count the # of accounts
pop_vac_lic = land_cen_lic.groupby(['ward','pop_2010','vacant'], 
                                   as_index=False).agg({'account':'count'})

# Sort pop_vac_lic and print the results
sorted_pop_vac_lic = pop_vac_lic.sort_values(["vacant", "account", "pop_2010"], 
                                             ascending=[False, True, True])

# Print the top few rows of sorted_pop_vac_lic
print(sorted_pop_vac_lic.head())