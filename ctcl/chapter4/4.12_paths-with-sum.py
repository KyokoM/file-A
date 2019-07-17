# Return all downward paths through a tree whose nodes sum to a target value.

def paths_with_sum(binary_tree, target_sum):
    paths=[]
    _=paths_with_partial_sum(binary_tree, target_sum,0, paths)
    for path in paths:
        path=path.reverse()
    return paths
  
def paths_with_partial_sum(node, target_sum, now_sum,paths):
    if not node:
        return []
    candidates1=paths_with_partial_sum(node.left, target_sum, now_sum,paths)
    candidates2=paths_with_partial_sum(node.right, target_sum, now_sum,paths)
    for lis in candidates1:
        print(candidates1,lis)
        lis[0]+=node.value
        lis.append(node.name)
        if lis[0]==target_sum:
            paths.append(lis[1:])
    for lis in candidates2:
        lis[0]+=node.value
        lis.append(node.name)
        if lis[0]==target_sum:
            paths.append(lis[1:])
    if node.value==target_sum:
        paths.append([node.name])
    return candidates1+candidates2+[[node.value,node.name]]
    


class Node():
  def __init__(self, name, value, left=None, right=None):
    self.name, self.value, self.left, self.right = name, value, left, right

class ListDict(dict):
  def __missing__(self, key):
    return []

import unittest

class Test(unittest.TestCase):
  def test_paths_with_sum(self):
    bt=Node("A",4,Node("B",-2,Node("D",7),Node("E", 4)),
                  Node("C", 7,Node("F",-1,Node("H",-1),Node("I",2,Node("K",1))),
                              Node("G", 0,None,        Node("J", -2))))
    self.assertEqual(paths_with_sum(bt, 12), [["A", "C", "F", "I"]])
    self.assertEqual(paths_with_sum(bt, 2), [['B', 'E'], ['I'], ['F', 'I', 'K'], ['A', 'B']])
    self.assertEqual(paths_with_sum(bt, 9), [['C', 'F', 'I', 'K'], ['A', 'B', 'D'], ["A","C","F","H"],
         ["A","C","G","J"]])

if __name__ == "__main__":
  unittest.main()