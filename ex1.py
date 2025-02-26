class Node:
    def __init__ (self, new_data):
        self.data = new_data
        self.next = None

class LinkedList:
    def __init__ (self):
        self.head = None
    def append(self, new_node):
        current = self.head
        if current:
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node

# function to find out middle element
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

# Function for implementing the Binary
# Search on linked list
def binary_search(head, value):
    start = head
    last = None

    while True:

        # Find middle
        mid = middle(start, last)

        # If middle is empty
        if mid is None:
            return False

        # If value is present at middle
        if mid.data == value:
            return True

        # If start and last node are overlapping
        elif start == last:
            break

        # If value is more than mid
        elif mid.data < value:
            start = mid.next

        # If the value is less than mid.
        elif mid.data > value:
            last = mid

    # value not present
    return False


if __name__ == "__main__":
  
      # Create a hard-coded linked list:
    # 1 -> 4 -> 7 -> 8 -> 9 -> 10
    head = Node(1)
    head.next = Node(4)
    head.next.next = Node(7)
    head.next.next.next = Node(8)
    head.next.next.next.next = Node(9)
    head.next.next.next.next.next = Node(10)

    value = 7
    if binary_search(head, value):
        print("Present")
    else:
        print("Value not present")