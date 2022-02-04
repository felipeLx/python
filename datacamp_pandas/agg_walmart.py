import pandas as pd
import numpy as np

sales = pd.DataFrame({
    "store": [1, 2, 3, 4, 5],
    "type": ["A","A","A","A","A"],
    "date": ["2010-02-05","2010-02-05","2010-02-05","2010-02-05","2010-02-05"],
    "weekly_sales": [24925.50, 50605.27, 13740.14, 39954.04, 32229.38],
    "is_holiday": [False,False,False,False,False],
    "temp_c": [5.73,5.73,5.73,5.73,5.73],
    "fuel_price": [0.679,0.679,0.679,0.679,0.679],
    "unemp": [8.106,8.106,8.106,8.106,8.106]
})

print(sales.head())
print(sales.info())
print(sales["weekly_sales"].mean())
print(sales["weekly_sales"].median())

print(sales["date"].max())
print(sales["date"].min())

def iqr(column):
    return column.quantile(0.75) - column.quantile(0.25)
print(sales["temperature_c"].agg(iqr))

def iqr(column):
    return column.quantile(0.75) - column.quantile(0.25)
print(sales[["temperature_c", "fuel_price_usd_per_l", "unemployment"]].agg(iqr))

# Update to print IQR and median of temperature_c, fuel_price_usd_per_l, & unemployment
print(sales[["temperature_c", "fuel_price_usd_per_l", "unemployment"]].agg([iqr, np.median]))

# Sort sales_1_1 by date
sales_1_1 = sales_1_1.sort_values(by="date")

# Get the cumulative sum of weekly_sales, add as cum_weekly_sales col
sales_1_1["cum_weekly_sales"] = sales["weekly_sales"].cumsum()

# Get the cumulative max of weekly_sales, add as cum_max_sales col
sales_1_1["cum_max_sales"] = sales["weekly_sales"].cummax()

# See the columns you calculated
print(sales_1_1[["date", "weekly_sales", "cum_weekly_sales", "cum_max_sales"]])