import timeit, matplotlib.pyplot as plt
class Node:
    def __init__(self, value):
        self._value = value
        self._next = None
    def getData(self):
        return self._value
    def setData(self, value):
        self._value = value
    def getNext(self):
        return self._next
    def setNext(self, next):
        self._next = next

class Linked_List:
    def __init__(self):
        self.head = None
    def insert_head(self, node):
        if self.head is not None:
            node.next = self.head
        self.head = node
    def insert_tail(self, node):
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current._next:
                current = current.getNext()
            current.setNext(node)
    def get_size(self):
        size = 0
        current = self.head
        while current is not None:
            size += 1
            current = current.getNext()
        return size
    def get_element_at_pos(self, pos):
        i = 0
        current = self.head
        while i != pos:
            i += 1
            current = current.getNext()
        return current.getData()
    def reverse(self):
        newhead = None
        prevNode = None
        for i in range(self.get_size() - 1, -1, -1):
            currNode = self.get_element_at_pos(i)
            currNewNode = Node(currNode)
            if newhead is None:
                newhead = currNewNode
            else:
                prevNode.setNext(currNewNode)
            prevNode = currNewNode
        self.head = newhead
    def new_reverse(self):
        prevNode = None
        currNode = self.head
        while currNode is not None:
            temp = currNode.getNext()
            currNode.setNext(prevNode)
            prevNode = currNode
            currNode = temp
        self.head = prevNode

def main():
    input_list = [1000, 2000, 3000, 4000]
    original_list = []
    optimized_list = []

    test_list = Linked_List()
    for num in input_list:
        print(f"Testing for {num} elements...")
        for i in range(test_list.get_size(), num):
            test_list.insert_tail(Node(i))
        original_list.append(timeit.timeit(lambda: test_list.reverse(), number = 100))
        optimized_list.append(timeit.timeit(lambda: test_list.new_reverse(), number = 100))

    
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
