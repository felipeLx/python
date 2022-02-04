import pandas as pd

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

# Drop duplicate store/type combinations
store_types = sales.drop_duplicates(subset=["store", "type"])
print(store_types.head())

# Drop duplicate store/department combinations
store_depts = sales.drop_duplicates(subset=["store", "department"])
print(store_depts.head())

# Subset the rows where is_holiday is True and drop duplicate dates
holiday_dates = sales[sales["is_holiday"] == True].drop_duplicates("date")

# Print date col of holiday_dates
print(holiday_dates["date"])