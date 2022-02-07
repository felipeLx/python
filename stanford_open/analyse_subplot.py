# subplot to help us examine the relationship between 2 variable over time
# alternative method, know as resampling, that we can use to accomplish the same task
# resampling when you change the frequency of your time series observations
apple.price.resample('M').mean()
apple.volume.resample('M').mean()

# after resampled both the price and volume data, combine the results into a single DataFrame, so that we can
# study realtionsip between price and volume
monthly_price = apple.price.resample('M').mean()
monthly_volume = apple.volume.resample('M').mean()

pd.concat([monthly_price, monthly_volume], axis='columns')
# this case, we want to combined along the columns axis, meaning that we want them side-by-side
monthly = pd.concat([monthly_price, monthly_volume], axis='columns')
monthly.plot()
plt.show()

# different scales from y-axis, because different scales we cant actually see the price trend
# solution is to separate plots with independents y-axis
monthly.plot(subplot=True)
plt.show()

# Calculate the annual rate of drug-related stops
print(ri.drugs_related_stop.resample('A').mean())

# Save the annual rate of drug-related stops
annual_drug_rate = ri.drugs_related_stop.resample('A').mean()

# Create a line plot of 'annual_drug_rate'
annual_drug_rate.plot()

# Display the plot
plt.show()

# Calculate and save the annual search rate
annual_search_rate = ri.search_conducted.resample('A').mean()

# Concatenate 'annual_drug_rate' and 'annual_search_rate'
annual = pd.concat([annual_drug_rate, annual_search_rate], axis='columns')

# Create subplots from 'annual'
annual.plot(subplots=True)

# Display the subplots
plt.show()