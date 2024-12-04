import pandas as pd

df = pd.read_csv("input.csv")

array_a = df['A'].values 
array_b = df['B'].values 

dictionary = {key: 0 for key in array_b}

for element in array_b:
    dictionary[element] += 1

total = 0

for element in array_a:
    if element in dictionary:
        total += element * dictionary[element]

print(total)