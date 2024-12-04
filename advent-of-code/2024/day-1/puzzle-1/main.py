import pandas as pd

df = pd.read_csv("input.csv")

def quick_sort(arr):
    if len(arr) <= 1:  
        return arr
    else:
        pivot = arr[0]  
        less_than_pivot = [x for x in arr[1:] if x <= pivot]  
        greater_than_pivot = [x for x in arr[1:] if x > pivot]  

        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

array_a = df['A'].values 
array_b = df['B'].values 

sorted_a = quick_sort(array_a)
sorted_b = quick_sort(array_b)

tot = 0

for i in range(len(sorted_a)):
    if sorted_a[i] > sorted_b[i]:
        tot += sorted_a[i] - sorted_b[i]
    else:
        tot += sorted_b[i] - sorted_a[i]

print(tot)