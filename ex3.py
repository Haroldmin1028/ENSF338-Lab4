"""
1.  Identify and explain the strategy used to grow arrays when full, with
    references to specific lines of code in the file above. What is the
    growth factor? 

    When a dynamic array is full in python, to grow the array, it used a strategic over-allocation method as shown in line 70
    of the 'list.c' file. Doing so, the capacity gets increased to avoid frequent memory allocations.
    By looking at that line of code, we are able to notice that:

newsize: the required size of the list

>> : bitwise right shift by 3 bits. Equivalent to dividing by 2^3 (this is how we figure out our growth factor).

+6 : this is a buffer that handles minor growth

& ~(size_t)3 : this Rounds the result to a multiple of 4 for allignment

Finally, to compute the size of memory allocated, you would compute:

newsize + newsize/2^3 +6 = size of allocation. If this value is not a multiple of 4, it will
round down to the nearest multipe of 3 due to the &~3 operation.

5.  Plot the distribution of both measurements (you can use hist or similar). Do you see any difference? Why?

    Yes, there is a difference. We see a difference because resizing arrays (S -> S+1) requires memory allocation 
    and copying which uses up more space and lengthens the amount of time required to complete the task. (S-1 -> S) 
    on the other hand has the capacity to lengthen the array so it's a lot more efficient 
"""

import sys
import time
import numpy as np
import matplotlib.pyplot as plt

memory_test = []

previous_capacity = sys.getsizeof(memory_test)

print(f"The initial size of the list that is empty is {memory_test} bytes")

for i in range(64):
    memory_test.append(i)
    new_capacity = sys.getsizeof(memory_test)
    if(new_capacity != previous_capacity):
        print(f"Memory has changed at {i+1} elements and has a capacity of {new_capacity} bytes")
        previous_capacity = new_capacity


S = 53  

times_S_to_S1 = []
for _ in range(1000):
    lst = list(range(S))  
    start = time.perf_counter()
    lst.append(S)  
    end = time.perf_counter()
    times_S_to_S1.append(end - start)

times_S1_to_S = []
for _ in range(1000):
    lst = list(range(S-1))  
    start = time.perf_counter()
    lst.append(S-1)  
    end = time.perf_counter()
    times_S1_to_S.append(end - start)


mean_S_to_S1 = np.mean(times_S_to_S1)
mean_S1_to_S = np.mean(times_S1_to_S)

print(f"Average time for S → S+1: {mean_S_to_S1:.10f} seconds")
print(f"Average time for S-1 → S: {mean_S1_to_S:.10f} seconds")

plt.figure(figsize=(10, 5))
plt.hist(times_S_to_S1, bins=30, alpha=0.7, label="S → S+1 (resize needed)")
plt.hist(times_S1_to_S, bins=30, alpha=0.7, label="S-1 → S (no resize)")
plt.xlabel("Time (seconds)")
plt.ylabel("Frequency")
plt.title("Distribution of List Growth Times")
plt.legend()
plt.show()