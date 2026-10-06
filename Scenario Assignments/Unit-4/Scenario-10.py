import numpy as np
import pandas as pd

# Create NumPy array of room rents
rents = np.array([2500, 3500, 4500, 5000, 3000, 6000, 4000, 5500])

# Calculate room rent statistics
print("Mean Room Rent:", np.mean(rents))
print("Median Room Rent:", np.median(rents))
print("Maximum Room Rent:", np.max(rents))
print("Minimum Room Rent:", np.min(rents))

# Create Pandas DataFrame
data = {
    "Room": ["101", "102", "103", "104", "105", "106", "107", "108"],
    "Type": ["Single", "Double", "Deluxe", "Suite", "Single", "Suite", "Double", "Deluxe"],
    "Rent": [2500, 3500, 4500, 5000, 3000, 6000, 4000, 5500]
}

df = pd.DataFrame(data)

print("\nHotel Room Data:")
print(df)

# Display rooms having rent greater than ₹4000
print("\nRooms with Rent Greater Than ₹4000:")
print(df[df["Rent"] > 4000])

# OUTPUT:
# Mean Room Rent: 4250.0
# Median Room Rent: 4250.0
# Maximum Room Rent: 6000
# Minimum Room Rent: 2500
#
# Hotel Room Data:
#   Room    Type  Rent
# 0  101  Single  2500
# 1  102  Double  3500
# 2  103  Deluxe  4500
# 3  104   Suite  5000
# 4  105  Single  3000
# 5  106   Suite  6000
# 6  107  Double  4000
# 7  108  Deluxe  5500
#
# Rooms with Rent Greater Than ₹4000:
#   Room    Type  Rent
# 2  103  Deluxe  4500
# 3  104   Suite  5000
# 5  106   Suite  6000
# 7  108  Deluxe  5500
