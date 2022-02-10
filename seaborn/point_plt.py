# point plots -> show the mean of a quantitative variable for the observation in each category
# -> point plot uses the tips dataset and shows the average bill among smokers versus non-smokers

"""
points show mean of quantitative variable
vertical lines show 95% condidence intervals
"""

# we can be 95% sure that the true population mean in each group lies within the confidence interval show

"""
point plots x line plots
. mean of quantitative variable
. 95% of confidence intervals for the mean
. line plots are relational plot, so both the x and y-axis are quantitative variables

# Difference
. line plot has quantitative variable(usualy time) on x-axis
. point plot has categorical variable on x-axis
"""

import matplotlib.pyplot as plt
import seaborn as sns

sns.catplot(x="age", y="masculinity_important", data=masculinity_data, hue="feel_masculine", kind="point")

# when to compare within a category group and not between them
sns.catplot(x="age", y="masculinity_important", 
            data=masculinity_data, hue="feel_masculine", 
            kind="point", join=False)

from numpy import median

sns.catplot(x="age", y="masculinity_important", 
            data=masculinity_data, hue="feel_masculine", 
            kind="point", join=False,
            estimator=median)
# median is more robust to outliers, so if your dataset has a lot of outliers, the median may be a better statistic to use
sns.catplot(x="age", y="masculinity_important", 
            data=masculinity_data, hue="feel_masculine", 
            kind="point",capsize=0.2)
# capsize parameter equal tot he desired width of the caps
# ci=None to empty the interval

# exercise
sns.catplot(x="famrel", y="absences",
			data=student_data,
            kind="point",
            capsize=0.2, join=False)

sns.catplot(x="romantic", y="absences",
			data=student_data,
            kind="point",
            hue="school",
            ci=None,
            estimator=median)