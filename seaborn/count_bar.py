# categorical plots: count plots and bar plots

# categorical variable: consists of a fixed, typically small number of possible values, or categories
"""
. examples: count plot, bar plots
. involve a categorical variable

these types of plots are commonly used when we want to make comparisons between different groups
"""
# catplot()

"""
easy to create subplots if we need to using the same "col" and "row" parameters
. used to create categorical plots
. same advantages of relplot()
. easily create subplots with col= and rol=
"""

import matplotlib.pyplot as plt
import seaborn as sns

sns.countplot(x="how_masculine", data=masculinity_data, kind="count")
# more sense for the categories to be in order from more to few / custom order

# custom order
# -> create a list of the order you want
category_order = ["No answer", "Not at all", "Not very", "Somewhat", "Very"]

sns.countplot(x="how_masculine", data=masculinity_data, kind="count", order=category_order)

# bar plots
# -> they show the mean of a quantitative varible among observations in each category
# display mean of quantitative variable per category
sns.catplot(x="day", y="total_bill", data=tips, kind="bar")
# lines show 95% confidence intervals for the mean
# shows uncertainly about our estimate
# assumes our data in a random sample
sns.countplot(x="day", y="total_bill", data=tips, kind="bar", ci=None)

# change orientation
sns.carplot(x="total_bill", y="day", data=tips, kind="bar")

# exercise
sns.catplot(x="Internet usage", data=survey_data,
            kind="count")

sns.catplot(y="Internet usage", data=survey_data,
            kind="count")

# Separate into column subplots based on age category
sns.catplot(y="Internet usage", col="Age Category", data=survey_data,
            kind="count")

sns.catplot(x="Gender", y="Interested in Math", data=survey_data, kind="bar")

# exercise
sns.catplot(x="study_time", y="G3", ci=None,
            data=student_data,
            kind="bar",
            order=category_order)
