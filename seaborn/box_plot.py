# boxplot: show the distribution of quantitative data
# see the median , spread, skewness, and outliers
# facilitates comparisons between groups
import matplotlib.pyplot as plt
import seaborn as sns

order_box=["Dinner", "Lunch"]
g = sns.catplot(x="time", y="total_bill", data=tips, kind="box", order=order_box)

# sym="" -> to ommit the outlier from the graphic
g = sns.catplot(x="time", y="total_bill", data=tips, kind="box", order=order_box, sym="")

# by default: the whiskers extend to 1 point 5 times the interquartile range, or IQR
    # whiskers extend to 1.5 * the interquartile range
    # make them extend to 2.0 * IQR: whis=2.0
# show the 5th and 95th percentiles: whis=[5,95]
# show min and max values: whis=[0, 100]
g = sns.catplot(x="time", y="total_bill", data=tips, kind="box", whis=[0,100])

# exercise
study_time_order = ["<2 hours", "2 to 5 hours", 
                    "5 to 10 hours", ">10 hours"]

# Create a box plot and set the order of the categories
sns.catplot(data=student_data, x="study_time", y="G3", order=study_time_order, kind="box")

# Create a box plot with subgroups and omit the outliers
sns.catplot(data=student_data, x="internet", y="G3", kind="box", sym="", hue="location")

# Extend the whiskers to the 5th and 95th percentile
sns.catplot(x="romantic", y="G3",
            data=student_data,
            kind="box",
            whis=[5,95])

# Set the whiskers at the min and max values
sns.catplot(x="romantic", y="G3",
            data=student_data,
            kind="box",
            whis=[0, 100])
