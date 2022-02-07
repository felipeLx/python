female_and_arrested = ri[(ri['driver_gender'] == 'F') & 
            (ri['is_arrested'] == True)]

# each condition is surronded by parentheses
# apersand (&) represents and operator

female_or_arrested = ri[(ri.driver_gender == 'F') | 
            (ri.is_arrested == True)]

# correlation, not causation
# analyze the relationship between gender and stop outcomes
    # assess whether there is a correlation
# not going to draw any conclusions about causation
    # would need additional data and expertise
# Create a DataFrame of female drivers stopped for speeding

female_and_speeding = ri[(ri.driver_gender == 'F') & (ri.violation == 'Speeding')]

# Create a DataFrame of male drivers stopped for speeding
male_and_speeding = ri[(ri.driver_gender == 'M') & (ri.violation == 'Speeding')]

# Compute the stop outcomes for female drivers (as proportions)
print(female_and_speeding.stop_outcome.value_counts(normalize=True))

# Compute the stop outcomes for male drivers (as proportions)
print(male_and_speeding.stop_outcome.value_counts(normalize=True))
