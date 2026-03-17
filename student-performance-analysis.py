import pandas as pd
import matplotlib.pyplot as plt

# 1. Data load
data = pd.read_csv("students.csv")

print("---- Student Data ----")
print(data)

# 2. Total & Average calculate
data['Total'] = data['Maths'] + data['Science'] + data['English']
data['Average'] = data['Total'] / 3

print("\n---- With Total & Average ----")
print(data)

# 3. Topper find
topper = data.loc[data['Total'].idxmax()]
print("\nTopper is:", topper['Name'])

# 4. Graph (Average marks)
plt.bar(data['Name'], data['Average'])
plt.title("Average Marks of Students")
plt.xlabel("Students")
plt.ylabel("Average Marks")
plt.show()