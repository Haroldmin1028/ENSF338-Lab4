import numpy as np, timeit, matplotlib.pyplot as plt

class Node:
    def __init__(self, value):
        self._value = value
        self.next = None

def reverse(self):
    newhead = None
    prevNode = None
    for i in range(self.get_size() - 1, -1, -1):
        currNode = self.get_element_at_pos(i)
        currNewNode = Node(currNode.data)
        if newhead is None:
            newhead = currNewNode
        else:
            prevNode.next = currNewNode
        prevNode = currNewNode
    self.head = newhead

def new_reverse(self):
    pass

def main():
    input_list = [1000, 2000, 3000, 4000]
    original_list = []
    optimized_list = []
    for num in input_list:
        original_list.append(timeit.timeit())
    
    plt.xlabel("Number of Elements")
    plt.ylabel("Time")
    plt.title("Original Reverse")
    plt.subplot(1, 2, 1)
    plt.plot(input_list, original_list)
    plt.subplot(1, 2, 2)
    plt.plot(input_list, optimized_list)
    plt.show()
    

if __name__ == "__main__":
    main()
