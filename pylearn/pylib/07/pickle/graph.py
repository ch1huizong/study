#! /usr/bin/env python
# -*- coding:UTF-8 -*-

# 看不太懂啊？ 回来研究

import pickle

class Node(object):
    def __init__(self,name):
        self.name = name
        self.connections = []

    def add_edge(self,node):
        self.connections.append(node)

    def __iter__(self):
        return iter(self.connections)

def preorder_traversal(root, seen=None, parent=None):
    if seen is None:
        seen = set()
    yield (parent, root)

    if root in seen:
        return
    seen.add(root)
    for node in root:
        for parent, subnode in preorder_traversal(node,seen, root):
            yield (parent, subnode)

def show_edges(root):
    for parent, child in preorder_traversal(root):
        if not parent:
            continue
        print "%5s -> %2s (%s)" %  \
                (parent.name, child.name, id(child))

root = Node('root')
a = Node('a')
b = Node('b')
c = Node('c')

root.add_edge(a)
root.add_edge(b)
a.add_edge(b)
b.add_edge(a)
b.add_edge(c)
a.add_edge(a)

print "Origin Graph:"
show_edges(root)

dumped = pickle.dumps(root)
reloaded = pickle.loads(dumped)

print "\nReloaded Graph:"
show_edges(reloaded)

