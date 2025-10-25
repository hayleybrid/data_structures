# find the middle node of a linked list, if the number of nodes is even, return the second middle node

class Node:
    def __init__(self, val, next=None):
        self.data = val
        self.next = next

def find_middle(head: Node) -> int:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow.val

def build_linked_list(nodes, f):...


if __name__ == "__main__":...