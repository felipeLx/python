import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("./airbnb_2.csv")
print(df.info())

df_count = df["neighbourhood_group"].value_counts(sort=True, ascending=False)
# print(df_count)

df_three = df[df["neighbourhood_group"].isin(["Manhattan", "Brooklyn", "Queens"])]

print(df_three)

df_bigger = df.groupby(["calculated_host_listings_count"])["neighbourhood_group"].value_counts(ascending=False)
df.groupby(["calculated_host_listings_count"])["neighbourhood_group"].value_counts(normalize=True)
print(df_bigger)

df.info()
df["revenue"] = df["price"] * df["number_of_reviews"]

data_plot = df.groupby(["neighbourhood_group"])["revenue"].mean()
data_plot.plot(kind="bar", rot=45)

man = df["neighbourhood_group"] == "Manhattan"
bro = df["neighbourhood_group"] == "Brooklyn"
que = df["neighbourhood_group"] == "Queens"
# df.reset_index(inplace=True)
filtered_df = df[man | bro | que]
filtered_df.groupby(["neighbourhood_group", "neighbourhood"])["revenue"].sum().nlargest(9).sort_values(ascending=False)

fil_room_df = filtered_df.groupby(["neighbourhood", "room_type"])["revenue"].sum().nlargest(9).sort_values(ascending=False)
fil_room_df.plot(kind="bar")
plt.title("Avg Revenue of the Neighbourhood by Room Type")