# Remove the duplicate values from a linked list.
# TODO(@KyokoM) 
# remove the code for the last part
# think the way not to use buffer
import unittest

def remove_duplicates(head):
  datas={}
  headNow=head
  datas[headNow.data]=True
  while(headNow.next.next):
    if headNow.next.data in datas:
      headNow.next=headNow.next.next
      if headNow.next.next==None:
        break
      continue
    else:
      datas[headNow.next.data]=True
    headNow=headNow.next
  if headNow.next.data in datas:
    headNow.next=None

class Node():
  def __init__(self, data, next):
    self.data = data
    self.next = next

class Test(unittest.TestCase):
  def test_remove_duplicates(self):
    head = Node(1,Node(3,Node(3,Node(1,Node(5,None)))))
    remove_duplicates(head)
    self.assertEqual(head.data, 1)
    self.assertEqual(head.next.data, 3)
    self.assertEqual(head.next.next.data, 5)
    self.assertEqual(head.next.next.next, None)

if __name__ == "__main__":
  unittest.main()