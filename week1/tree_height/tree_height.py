# python3

import sys
import threading
from queue import *

# My implementation
def compute_height(n, parents):
    root = -1
    nodes = [None] * (n) 
    for i in range(n):
        nodes[i] = []
    for i in range(n):
        if parents[i] != -1:
            nodes[parents[i]] += [i]
        else:
            root = i

    height = 0
    q = Queue()
    q.put((nodes[root], 1))
    while not q.empty():
        node = q.get()
        if len(node[0]) > 0 :
            for i in node[0]:
                if len(nodes[i]) > 0:
                    q.put((nodes[i], node[1]+1))
            height = max(height, node[1]+1)

    return height

def original_computer_height(n, parents):
    max_height = 0
    for vertex in range(n):
        height = 0
        current = vertex
        while current != -1:
            height += 1
            current = parents[current]
        max_height = max(max_height, height)
    return max_height

# Just making notes -> BST alphabetical
def in_order_traversal(tree):
    if tree == None:
        return
    in_order_traversal(tree.left)
    print(tree.key)
    in_order_traversal(tree.right)

# DFS -> Notes
def pre_order_traversal(tree):
    if tree == None:
        return
    print(tree.key)
    pre_order_traversal(tree.left)
    pre_order_traversal(tree.right)

# DFS -> Notes
def post_order_traversal(tree):
    if tree == None:
        return
    post_order_traversal(tree.left)
    post_order_traversal(tree.right)
    print(tree.key)

# BFS -> Notes
def level_traversal(tree):
    if tree == None:
        return
    q = Queue()
    q.put(tree)
    while not q.empty():
        node = q.get()
        if node.left != None:
            q.put(node.left)
        if node.right != None:
            q.put(node.right)

def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
