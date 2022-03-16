import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

df_ch = pd.read_csv('./chn_data.csv')
df_ch = df_ch.loc[:, ~df_ch.columns.str.contains('^Unnamed')]

df_br = pd.read_csv('./bra_data.csv')
df_br = df_br.loc[:, ~df_br.columns.str.contains('^Unnamed')]

df_za = pd.read_csv('./zaf_data.csv')
df_za = df_za.loc[:, ~df_za.columns.str.contains('^Unnamed')]

df_ru = pd.read_csv('./rus_data.csv')
df_ru = df_ru.loc[:, ~df_ru.columns.str.contains('^Unnamed')]

df_in = pd.read_csv('./ind_data.csv')
df_in = df_in.loc[:, ~df_in.columns.str.contains('^Unnamed')]

sns.set_theme(style="darkgrid")

data_leaks = [df_ch, df_br, df_in, df_ru, df_za]
countries = ["China", "Brazil", "India", "Rusia", "South Africa"]

for i in data_leaks:
    country_name = i["Country Name"].unique()
    g = sns.relplot(x="Air transport, passengers carried",
            y="Inflation, consumer prices (annual %)", 
            data=i,
            kind="scatter", 
            hue="Year").set(title= country_name + " Number of passengers x Inflation")


"""
labels = df_ch['Year'].unique()
chn_inf = df_ch["Inflation, consumer prices (annual %)"].unique()
bra_inf = df_br["Inflation, consumer prices (annual %)"].unique()
ind_inf = df_in["Inflation, consumer prices (annual %)"].unique()
zaf_inf = df_za["Inflation, consumer prices (annual %)"].unique()
rus_inf = df_ru["Inflation, consumer prices (annual %)"].unique()
"""
"""
chn_gdp = df_ch["GDP per capita growth (annual %)"].unique()
bra_gdp = df_br["GDP per capita growth (annual %)"].unique()
ind_gdp = df_in["GDP per capita growth (annual %)"].unique()
zaf_gdp = df_za["GDP per capita growth (annual %)"].unique()
rus_gdp = df_ru["GDP per capita growth (annual %)"].unique()
"""
"""
x = np.arange(len(labels))  # the label locations
width = 0.20  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x, chn_inf, width, label='China')
rects2 = ax.bar(x + .20, bra_inf, width, label='Brazil')
rects3 = ax.bar(x + .40, ind_inf, width, label='India')
rects4 = ax.bar(x + .60, zaf_inf, width, label='South Africa')
rects5 = ax.bar(x + .80, rus_inf, width, label='Rusia')

ax.set_ylabel('Inflation (annual %')
ax.set_title('Inflation, consumer prices (annual %)')
"""

"""
ax.set_ylabel('GDP % Growth')
ax.set_title('Growth of GDP per capita')

ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

plt.xticks(rotation=90)
fig.tight_layout()
"""
plt.show()
"""
def autolabel(rects):
    # Attach a text label above each bar in *rects*, displaying its height.
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)
autolabel(rects3)
autolabel(rects4)
autolabel(rects5)
"""

"""
print(labels)
men_means = [20, 34, 30, 35, 27]
women_means = [25, 32, 34, 20, 25]

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, men_means, width, label='Men')
rects2 = ax.bar(x + width/2, women_means, width, label='Women')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()


def autolabel(rects):
    # Attach a text label above each bar in *rects*, displaying its height.
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects1)
autolabel(rects2)

fig.tight_layout()

plt.show()
"""