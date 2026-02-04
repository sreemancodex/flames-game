import pandas 



# Create your first simple dataset
data = {
    "Name": ["Alice", "Bob", "Charlie", "Diana"],
    "Age": [24, 30, 22, 28],
    "Score": [85, 90, 78, 92]
}
df = pandas.DataFrame(data)

print(df)