"""
Identify and explain the strategy used to grow arrays when full, with
references to specific lines of code in the file above. What is the
growth factor? [0.1 pts

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
"""