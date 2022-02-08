# statistical plotting is a set of methods for using visualization to make comparisons

# adding error bars to bar charts
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

ax.bar("Rowing", mens_rowing["Height"].mean(),
    yerr=mens_rowing["Height"].std())

# yerr -> additional markers on a plot or bar chart that tell us something about the distribution of the data
ax.bar("Gymnastics", mens_gym["Height"].mean(),
    yerr=mens_gym["Height"].std())

ax.set_ylabel("Height")
plt.show()

# error bars instead summarize the distribution of the data in one number, such as the std deviation of the values
# add the error bar as argument to a bar chat

"""
histograms in two numbers: the meal value, and the spread of values, quantified as the standard deviation
"""
ax.errorbar(s_weather["MONTH"], s_weather["MLY-TAVG-NORMAL"], yerr=s_weather["MLY-TAVG-STDDEV"])
ax.errorbar(a_weather["MONTH"], a_weather["MLY-TAVG-NORMAL"], yerr=a_weather["MLY-TAVG-STDDEV"])
ax.set_ylabel("Temp (Fº)")
plt.show()

# add the error 
ax.boxplot([mens_row["Height"], mens_gym["Height"]])
# pass the list to the method, because the boxplot doesn't know the labels on each of the variables,
# we add separately, labelling the y-axis as well
ax.set_xticklabels(["Row", "Gym"])
ax.set_ylabel("Height")
plt.show()
# red line indicates the median height
# the edges of the box portion at the center indicate the inter-quartile range of the data, between 
# the 25-quartile and the 75-quartile percentiles
# the whiskers at the ends of the thin bars indicate one and a half times, that indicate
    # the size of the inter-quartile range beyond the 75th and 25th quartile