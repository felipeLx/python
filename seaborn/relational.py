# Seaborn calls plots that visualize relationship as "relational plots"

# creating separate plot per subgroup
# relplot() -> stand to relational plot
# advantage to create subplots in a single figure
import seaborn as sns
import matplotlib.pyplot as plt

sns.relplot(x="total_bill", y="tip", data="tips", kind="scatter")

# if you want to arrange these vertically or horizontal: use the row= or col=
sns.relplot(x="total_bill", y="tip", data="tips", kind="scatter", col="smokers")

# or use in the same plot
sns.relplot(x="total_bill", y="tip", data="tips", kind="scatter", col="smokers", row="time")

# define how many plots you want to row
sns.relplot(x="total_bill", y="tip", data="tips", kind="scatter", col="day", col_wrap="2")

# also can define the order, using col_order= or row_order=
sns.relplot(x="total_bill", y="tip", data="tips", kind="scatter", col="day", col_wrap="2", col_order=["Thur", "Fri", "Sat", "Sun"])

# exercise
sns.relplot(x="absences", y="G3", 
            data=student_data,
            kind="scatter", 
            row="study_time")

# exercise1
sns.relplot(x="G1", y="G3", 
            data=student_data,
            kind="scatter", 
            col="schoolsup",
            col_order=["yes", "no"])

# exercise2
sns.relplot(x="G1", y="G3", 
            data=student_data,
            kind="scatter", 
            col="schoolsup",
            col_order=["yes", "no"],
            row="famsup",
            row_order=["yes", "no"])