import matplotlib.pyplot as plt

# subplots create 2 plots
fig, ax = plt.subplots(3, 2)
# small multiples

# small multiples are typically arranged on the page as a grid with rows and columns
# .subplots(3,2)
# creating a Figure object with 3 rows of subplots, and 2 columns
# ax now is an array of Axes objects 
ax[0,0].plot(a_weather["MONTH"], a_weather["MLY-TAVG-NORMAL"], color='r')

# special case
fig, ax = plt.subplots(2,1)
# array will be one-dimensional, will only have to provide one index to access the elements of this array
ax[0].plot(s_weather["MONTH"], s_weather["MLY-PRCP-NORMAL"], color='b')
ax[0].plot(s_weather["MONTH"], s_weather["MLY-PRCP-25PCTL"], color='b', linestyle='--')
ax[0].plot(s_weather["MONTH"], s_weather["MLY-PRCP-75PCTL"], color='b', linestyle='--')

ax[1].plot(a_weather["MONTH"], a_weather["MLY-PRCP-NORMAL"], color='r')
ax[1].plot(a_weather["MONTH"], a_weather["MLY-PRCP-25PCTL"], color='r', linestyle='--')
ax[1].plot(a_weather["MONTH"], a_weather["MLY-PRCP-75PCTL"], color='r', linestyle='--')

ax[0].set_ylabel("Precipitation (inches)")
ax[0].set_ylabel("Precipitation (inches)")

fix, ax = plt.subplots(2, 1, sharey=True)
# sharey -> to make sure that all the subplots have the same range of y-axis values
