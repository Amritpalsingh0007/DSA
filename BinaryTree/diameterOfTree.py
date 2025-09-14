from binaryTree import Node

"""
Diameter of a tree is longest path between any two Nodes (may or may not include root).
"""
max_path_length = 0
def findDiameter(node):
    global max_path_length
    if node == None:
        return 0
    
    l = findDiameter(node.left)
    r = findDiameter(node.right)
    max_path_length = max(max_path_length, l + r)
    return 1 + max(l, r)

#Creating Binary Tree
drinks = Node("drinks")
hot = Node("hot")
cold = Node("cold")
tea = Node("tea")
coffee = Node("coffee")
cola = Node("cola")
fanta = Node("fanta")

drinks.left = hot
drinks.right = cold
hot.left = tea
hot.right = coffee
cold.left = cola
cold.right = fanta

print(findDiameter(drinks))
print(max_path_length)

root = Node(1)
root.left = Node(2)
root.left.left = Node(3)
root.left.right = Node(1)
root.right = Node(1)
root.right.left = Node(3)
root.right.right = Node(6)
root.right.left.left = Node(1)
root.right.left.left.left = Node(1)
root.right.left.left.right = Node(2)
root.right.left.left.left.left = Node(6)
root.right.left.left.left.left.right = Node(8)
root.right.right.right = Node(9)
root.right.right.right.right = Node(10)
root.right.right.right.right.left = Node(5)

findDiameter(root)
print(max_path_length)