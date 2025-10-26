#binary tree level order traversal
#given a binary tree, return its level order traversal. the input is the root node of the tree, the output should be a list of integers
#with the ith list containing values of nodes on level i, from left to right

from collections import deque

class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def level_order_traversal(root: Node) -> list[list[int]]:
    res = []
    queue = deque([root])
    while len(queue) > 0:
        n = len(queue)
        new_level = []
        for _ in range(n):
            node = queue.popleft()
            new_level.append(node.val)
            for child in [node.left, node.right]:
                if child is not None:
                    queue.append(child)
        res.append(new_level)
    return res

def build_tree(nodes, f=int):
    if not nodes:
        return None
    root = Node(f(nodes[0]))
    queue = deque([root])
    i = 1
    while queue and i < len(nodes):
        current = queue.popleft()
        if i < len(nodes) and nodes[i] is not None:
            current.left = Node(f(nodes[i]))
            queue.append(current.left)
        i += 1
        if i < len(nodes) and nodes[i] is not None:
            current.right = Node(f(nodes[i]))
            queue.append(current.right)
        i += 1
    return root

if __name__ == "__main__":
    raw = input("Enter tree nodes in level order (use None for missing nodes, separated by spaces):\n")
    parts = [None if x == "None" else x for x in raw.split()]
    root = build_tree(parts, f=int)
    result = level_order_traversal(root)
    print("Level order traversal:", result)


