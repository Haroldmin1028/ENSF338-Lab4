import timeit
from numpy import random
import matplotlib.pyplot as plt
import scipy
import numpy as np

class Node:
    def __init__ (self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__ (self, head):
        self.head = None
    def insert(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        
        current = self.head
        while True:
            if current.next is None:
                current.next = node
                break
            current = current.next

class ArrayClass:
    def __init__(self):
        self.data = []

    def insert(self, data):
        self.data.append(data)

def binarySearch(arr, low, high, x):
        while low <= high:
            mid = low + (high - low) // 2
            if arr[mid] == x:
                return mid
            elif arr[mid] < x:
                low = mid + 1
            else:
                high = mid - 1
        return -1

def middle(start, last):
    if start is None:
        return None

    if start == last:
        return start

    slow = start
    fast = start.next

    while fast != last:
        fast = fast.next
        slow = slow.next
        if fast != last:
            fast = fast.next

    return slow


def binary_search(head, value):
    start = head
    last = None

    while True:
        mid = middle(start, last)
        if mid is None:
            return False     
        if mid.data == value:
            return True
        elif start == last:
            break
        elif mid.data < value:
            start = mid.next
        elif mid.data > value:
            last = mid

    return False


def measure_performance(sizes):
    array_times = []
    linked_list_times = []

    for size in sizes:
        data = np.sort(np.random.randint(0, size * 10, size))

        array = ArrayClass()
        linked_list = LinkedList(None)

        for num in data:
            array.insert(num)
            linked_list.insert(num)

        target = np.random.choice(data)

        array_time = timeit.timeit(lambda: binarySearch(array.data, 0, size - 1, target), number=10) / 10
        linked_list_time = timeit.timeit(lambda: binary_search(linked_list, target), number=10) / 10
        array_times.append(array_time)
        linked_list_times.append(linked_list_time)

    return array_times, linked_list_times

sizes = [1000, 2000, 4000, 8000]

array_times, linked_list_times = measure_performance(sizes)

plt.figure(figsize=(8, 5))
plt.plot(sizes, array_times, label="Array Binary Search", marker="o")
plt.plot(sizes, linked_list_times, label="Linked List Binary Search", marker="s")
plt.xlabel("Input Size")
plt.ylabel("Time (seconds)")
plt.title("Search Performance: Array vs. Linked List")
plt.legend()
plt.grid()
plt.show()

def main():
    return 0

if __name__ == "__main__":
    main()


'''
4.  You already know that complexity of binary search for array is O(logn). What 
    is the complexity of binary search for linked lists? (explain in your own 
    words, do not just copy/paste from sites above).

    The complexity of binary search for linked lists is O(n). This is because 
    memory is not stored contiguously as they are in arrays, so we will need to 
    traverse through all nodes before the desired node which has O(n) complexity. 


5.  Measure average-case performance of binary search in linked list and array 
    on inputs of size [1000, 2000, 4000, 8000]; plot performance for both in the 
    same figure, and interpolate with appropriate functions.


'''