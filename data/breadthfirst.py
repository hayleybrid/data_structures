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

def build_tree(nodes, f):...

if __name__ == "__main__":...


