# scatter plot overview
"""
subplots(col and row)
subgroups with color(hue)

subgroups with point size and style
changing point transparency

use with both: scatterplot or relplot()
"""

# size
sns.relplot(x="G1", y="G3", 
            data=student_data,
            kind="scatter", 
            col="schoolsup",
            col_order=["yes", "no"],
            size="size")

# style
# will use different point styles for each value of variable
style="smoker" # -> different point style in addition to a diff colors

# transparency
aplha=0.4
# value between 0 and 1

# exercise
# Create scatter plot of horsepower vs. mpg
sns.relplot(x="horsepower", y="mpg", hue="cylinders",
            data=mpg, kind="scatter", 
            size="cylinders")

# exercise2
sns.relplot(x="acceleration", y="mpg", hue="origin", data=mpg, style="origin", kind="scatter")
