# seaborn is a powerful Python library for creating data viz*
# easily create the most common types of plots
# why is seaborn useful?
    # explore
    # communicate results
# works extremely well with Pandas data structures

import seaborn as sns
import matplotlib.pyplot as plt

height = [62,64,69,75,66,68,65,71,76,73]
weight = [120,130,110,140,110,120,135,172,200,187]
gender = ["Female", "Female","Female","Female","Male","Male","Male","Male","Male","Male"]
sns.scatterplot(x=height, y=weight)
sns.countplot(x=gender)