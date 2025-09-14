from binaryTree import Node
from collections import deque

'''
1. DFS (Depth First Search)
    - Inorder
    - Preorder
    - Postorder
2. BFS (Breath First Search)
    - Level Order Traversal
'''

class DFS:
    def __init__(self, root):
        self.root = root
    
    def inorder(self, node):
        if node == None:
            # print("None ->", end="")
            return
        
        self.inorder(node.left)
        print(node.val, "->",end="")
        self.inorder(node.right)
    
    def preorder(self, node):
        if node == None:
            # print("None ->", end="")
            return
        
        print(node.val, "->",end="")
        self.preorder(node.left)
        self.preorder(node.right)
    
    def postorder(self, node):
        if node == None:
            # print("None ->", end="")
            return
        
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.val, "->",end="")

class BFS:
    def __init__(self, root):
        self.root = root
    
    def levelOrderTraversal(self):
        notVisitedNodes = [self.root]
        l = 0
        r = 0
        while(not l > r):
            print(notVisitedNodes[l].val, " -> ", end="")
            if notVisitedNodes[l].left:
                notVisitedNodes.append(notVisitedNodes[l].left)
                r += 1
            if notVisitedNodes[l].right:
                notVisitedNodes.append(notVisitedNodes[l].right)
                r += 1
            l += 1
    
    def levelOrderTraversalUsingDeque(self):
        queue = deque([])
        queue.append(self.root)
        result = []

        while(len(queue) != 0):
            e = queue.popleft()
            result.append(e.val)
            if e.left is not None:
                queue.append(e.left)
            if e.right is not None:
                queue.append(e.right)
    
        return result

# Tree Creation
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
# DFS Methods
dfs = DFS(drinks)
dfs.inorder(dfs.root)
print()
dfs.preorder(dfs.root)
print()
dfs.postorder(dfs.root)

print()
bfs = BFS(drinks)

bfs.levelOrderTraversal()
print()
print(" -> ".join(bfs.levelOrderTraversalUsingDeque()))