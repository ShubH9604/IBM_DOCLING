import pandas as pd
import re

# Step 1: Read the text file
with open("canara.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

# Step 2: Clean and split lines based on 2 or more spaces
data = []
for line in lines:
    line = line.strip()
    if not line:
        continue  # skip empty lines
    columns = re.split(r'\s{2,}', line)  # split on 2 or more spaces
    if len(columns) >= 3:  # adjust this if your lines have more or fewer columns
        data.append(columns)

# Step 3: Create DataFrame without headers
df = pd.DataFrame(data)

# Step 4: Save to Excel
df.to_excel("canara.xlsx", index=False, header=False)
print("✅ Converted 'canara.txt' to 'canara.xlsx'")