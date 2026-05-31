from typing import *

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.smallest_in_subtree = data
        self.largest_in_subtree = data
        self.max_gap_in_subtree = 0
        self.left = None
        self.right = None
        self.height = 1

def updateLeftChild(node, newChild):
    node.left = newChild
    if newChild is not None:
        node.smallest_in_subtree = newChild.smallest_in_subtree
        node.max_gap_in_subtree = max(
            node.data - newChild.largest_in_subtree,
            newChild.max_gap_in_subtree,
            max(
                node.right.smallest_in_subtree - node.data,
                node.right.max_gap_in_subtree
            ) if node.right is not None else 0
        )
    else:
        node.smallest_in_subtree = node.data
        node.max_gap_in_subtree = max(
            node.right.smallest_in_subtree - node.data,
            node.right.max_gap_in_subtree
        ) if node.right is not None else 0
    node.height = 1 + max(
        getHeight(node.left),
        getHeight(node.right)
    )

def updateRightChild(node, newChild):
    node.right = newChild
    if newChild is not None:
        node.largest_in_subtree = newChild.largest_in_subtree
        node.max_gap_in_subtree = max(
            newChild.smallest_in_subtree - node.data,
            newChild.max_gap_in_subtree,
            max(
                node.data - node.left.largest_in_subtree,
                node.left.max_gap_in_subtree
            ) if node.left is not None else 0
        )
    else:
        node.largest_in_subtree = node.data
        node.max_gap_in_subtree = max(
            node.data - node.left.largest_in_subtree,
            node.left.max_gap_in_subtree
        ) if node.left is not None else 0
    node.height = 1 + max(
        getHeight(node.left),
        getHeight(node.right)
    )

def getHeight(node):
    if not node:
        return 0
    return node.height

def getBalance(node):
    if not node:
        return 0
    return getHeight(node.left) - getHeight(node.right)

def rightRotate(y):
    x = y.left
    T2 = x.right
    updateLeftChild(y, T2)
    updateRightChild(x, y)
    return x

def leftRotate(x):
    y = x.right
    T2 = y.left
    updateRightChild(x, T2)
    updateLeftChild(y, x)
    return y

def insert(node, data):
    if not node:
        return TreeNode(data)

    if data < node.data:
        updateLeftChild(node, insert(node.left, data))
    elif data > node.data:
        updateRightChild(node, insert(node.right, data))

    # Update the balance factor and balance the tree
    node.height = 1 + max(getHeight(node.left), getHeight(node.right))
    balance = getBalance(node)

    # Balancing the tree
    # Left Left
    if balance > 1 and getBalance(node.left) >= 0:
        return rightRotate(node)

    # Left Right
    if balance > 1 and getBalance(node.left) < 0:
        node.left = leftRotate(node.left)
        return rightRotate(node)

    # Right Right
    if balance < -1 and getBalance(node.right) <= 0:
        return leftRotate(node)

    # Right Left
    if balance < -1 and getBalance(node.right) > 0:
        node.right = rightRotate(node.right)
        return leftRotate(node)

    return node    

def find_max_gap_to_left(node, target, greatest_lower_bound = 0):
    if node is None:
        return target - greatest_lower_bound
    if target < node.data:
        return find_max_gap_to_left(node.left, target, greatest_lower_bound)
    elif target > node.data:
        max_gap_immediate_left = node.data - node.left.largest_in_subtree if node.left is not None else node.data - greatest_lower_bound
        max_gap_left_subtree = node.left.max_gap_in_subtree if node.left is not None else 0
        if node.right is None:
            return max(
                max_gap_left_subtree,
                max_gap_immediate_left,
                target - node.data
            )
        elif node.right.smallest_in_subtree >= target:
            return max(
                max_gap_left_subtree,
                max_gap_immediate_left,
                target - node.data,
            )
        else:
            return max(
                max_gap_left_subtree,
                max_gap_immediate_left,
                node.right.smallest_in_subtree - node.data,
                find_max_gap_to_left(node.right, target, node.right.smallest_in_subtree)
            )
    else: # target == node.data
        if node.left is None:
            return target - greatest_lower_bound
        else:
            return max(
                target - node.left.largest_in_subtree,
                node.left.max_gap_in_subtree
            )


def inOrderTraversal(node):
    if node is None:
        return
    inOrderTraversal(node.left)
    print(node.data, end=", ")
    inOrderTraversal(node.right)

class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        obstacles = TreeNode(0)
        query_results = []
        for query in queries:
            if query[0] == 1:
                obstacles = insert(obstacles, query[1])
            else:
                query_results.append(query[2] <= find_max_gap_to_left(obstacles, query[1]))
        # inOrderTraversal(obstacles)

        return query_results



s = Solution()

print(
    s.getResults(
        [[1,135],[1,136],[1,121],[1,128],[1,77],[1,38],[1,109],[1,54],[1,90],[1,68],[1,103],[1,3],[1,47],[1,46],[1,145],[1,122],[1,101],[1,51],[1,67],[1,86],[2,77,39]]
    )
)