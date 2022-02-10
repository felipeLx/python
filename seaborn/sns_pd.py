import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("masculinity.csv")
sns.countplot(x="how_masculine", data=df)
plt.show()

"""
Unnamed: 0               How old are you?
    0     Marion                             12
    1      Elroy                             16
    2        NaN  What is your favorite animal?
    3     Marion                            dog
    4      Elroy                            cat

Is it tidy? 
No, because a single column contains different types of information.
"""

# adding a third variable with hue
# load dataset -> function in Seaborn and passing in the name of the dataset
tips = sns.load_dataset("tips")
tips.head()

sns.scatterplot(x="total_bill", y="tip", data="tips", hue="smoker", hue_order=["Yes", "No"])
# hue_order: takes in a list of values and will set the order of the values in the plot accordingly
# pallete: control the colors assigned to each value

hue_colors = {"Yes": "black", "No": "red"}
sns.scatterplot(x="total_bill", 
                y="tip", 
                data=tips, 
                hue="smoker",
                palette=hue_colors, 
                hue_order=["Yes", "No"])

# exercise
sns.scatterplot(x="absences", y="G3", 
                data=student_data, 
                hue="location",
                hue_order=["Rural", "Urban"])

# exercise II
palette_colors = {"Rural": "green", "Urban": "blue"}

# Create a count plot of school with location subgroups
sns.countplot(x="school", data=student_data, palette=palette_colors, hue="location")
