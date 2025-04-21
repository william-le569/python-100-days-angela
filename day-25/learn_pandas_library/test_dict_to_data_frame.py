import pandas as pd

# Your dictionary
color_dict = {"Black": 5, "Red": 10}

# Convert to DataFrame
df = pd.DataFrame(list(color_dict.items()), columns=["Color", "Count Color"])

print(list(color_dict.items()))


# Display the result
print(df)