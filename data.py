# IMPORTING LIBRARIES

import pandas as pd

# CONNECTING TO DATA SOURCE

data = pd.read_excel ("process_data.xlsx")

X_train = data.iloc[:, 1:5]

oa_flows = data.iloc[:, 5]
conversions = data.iloc[:, 8]
water_consumptios = data.iloc[:, 11]

print(X_train)
print(oa_flows)
print(conversions)
print(water_consumptios)