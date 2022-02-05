# subsetting and calculation on pivot tables
# recal to create pivot tables
dogs_height_by_breed_vs_color = dog_pack.pivot_table("height_cm", index="breed", columns="color")

# Pivot Tables are just DataFrames with sorted indexes
dogs_height_by_breed_vs_color.loc["Chow Chow": "Poodle"]

# the methods for calculating summary statistics on a DataFrame, such as mean, have an axis argument
dogs_height_by_breed_vs_color.mean(axis="index")
# means, calculate statistic across rows

# to calculate across column
dogs_height_by_breed_vs_color.mean(axis="columns")

# Get the worldwide mean temp by year
mean_temp_by_year = temp_by_country_city_vs_year.mean()

# Filter for the year that had the highest mean temp
print(mean_temp_by_year[mean_temp_by_year == mean_temp_by_year.max()])

# Get the mean temp by city
mean_temp_by_city = temp_by_country_city_vs_year.mean(axis="columns")

# Filter for the city that had the lowest mean temp
print(mean_temp_by_city[mean_temp_by_city == mean_temp_by_city.min()])