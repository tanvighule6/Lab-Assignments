import numpy as np
import pandas as pd

# Create NumPy array of product prices
prices = np.array([40, 60, 120, 80, 150, 200, 50, 90])

# Calculate price statistics
print("Mean Price:", np.mean(prices))
print("Median Price:", np.median(prices))
print("Maximum Price:", np.max(prices))
print("Minimum Price:", np.min(prices))

# Create Pandas DataFrame
data = {
    "Item": ["Rice", "Milk", "Bread", "Sugar", "Oil", "Biscuits", "Salt", "Tea"],
    "Price": [40, 60, 120, 80, 150, 200, 50, 90],
    "Quantity": [25, 8, 15, 6, 12, 5, 20, 7]
}

df = pd.DataFrame(data)

print("\nGrocery Store Data:")
print(df)

# Display items having quantity less than 10
print("\nItems with Quantity Less Than 10:")
print(df[df["Quantity"] < 10])

# OUTPUT:
# Mean Price: 98.75
# Median Price: 85.0
# Maximum Price: 200
# Minimum Price: 40
#
# Grocery Store Data:
#         Item  Price  Quantity
# 0       Rice     40        25
# 1       Milk     60         8
# 2      Bread    120        15
# 3      Sugar     80         6
# 4        Oil    150        12
# 5    Biscuits    200         5
# 6       Salt     50        20
# 7        Tea     90         7
#
# Items with Quantity Less Than 10:
#        Item  Price  Quantity
# 1      Milk     60         8
# 3     Sugar     80         6
# 5  Biscuits    200         5
# 7       Tea     90         7
