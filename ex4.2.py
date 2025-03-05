"""
• Now, consider the tasks of searching in a sorted array
3. Provide the code for an inefficient implementation and an efficient
implementation. [0.1 pts]
4. State the worst-case complexity of each. [0.1 pts]
5. Provide the code for an experiment that demonstrates the
difference. [0.1 pts] The experiment should:
1. Time the execution of both implementations on realistic, large inputs (1000
elements or above)
2. Plot the distribution of measured values across multiple measurements (>=
100 measurements per task)

4/3: 3. Considering searching in a sorted array, efficient method would be binary search and an inefficient method would be linear search.
     4. The worst case complexity for binary search (efficient method) is O(log n) and the worst case method for linear search (inefficient method) is O(n)
     The linear search is inefficient as it will check each and every element and compare it to the target value (until it is reached), regardless if it is sorted or not. Binary search works well
     with sorted arrays, as it splits bigger elements (in order) to the right and smaller elements (in order) to the left.
     5. Code for experiment is provided

"""

import timeit
import matplotlib.pyplot as plt
import random



def efficient_implementation(arr, value):
    left = 0
    right = len(arr) - 1
    while left<=right:
        mid = (left+right)//2
        if arr[mid] == value:
            return mid
        elif arr[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
    return -1 

def inefficient_implementation(arr, value):
    for i in range(len(arr)):
        if arr[i] == value:
            return i
    return -1


size_list = 1000
ordered_list = []
measurement_num = 100
inefficient_times = []
efficient_times = []

for i in range(size_list): # gives an ordered list from 0 to 999 (1000 elements)
    ordered_list.append(i)

for i in range(measurement_num):
    target_value = random.randint(0, size_list - 1) # gives random value from 0 to 999 (inclusive)

    inef_time = timeit.timeit(lambda: inefficient_implementation(ordered_list, target_value), number = 1)
    inefficient_times.append(inef_time) # Times and appends to inefficient_times

    eff_time = timeit.timeit(lambda: efficient_implementation(ordered_list, target_value), number = 1 )
    efficient_times.append(eff_time) # Times and appends to efficient_times

plt.figure(figsize=(10, 5))
plt.hist(inefficient_times, bins = 20, alpha=0.5, label="Inefficient Implementation", color="blue") # Actually plotting
plt.hist(efficient_times, bins = 20, alpha=0.5, label = "Efficient Implementation", color ="red") # Actually plotting

plt.xlabel("Execution Time (sec)")
plt.ylabel("Frequency")
plt.legend()
plt.title("Distribution of Measured Values: Ineficient vs Efficient")
plt.show()
