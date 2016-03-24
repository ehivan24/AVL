__author__ = 'edwingsantos'

from AVL.BalanceTree import BalanceTree

tree = BalanceTree()

tree.insert(4)
tree.insert(2)
tree.insert(3)
tree.insert(1)
tree.insert(5)
tree.insert(0)


tree.traverseInOrder()