# Return the k^{th} to last node in a linked list.
# TODO
# use xrange(x) instead of while(i<k and headNow!=None)
# think about k is larger than number of node
import unittest

def kth_to_last(head, k):
    headNow=head
    i=0
    while(i<k and headNow!=None):
        headNow=headNow.next
        i+=1
    pointerK=head
    if not headNow:
        return head
    while(headNow.next):
        headNow=headNow.next
        pointerK=pointerK.next
    return pointerK.next
    


class Node():
  def __init__(self, data, next=None):
    self.data, self.next = data, next

class Test(unittest.TestCase):
  def test_kth_to_last(self):
    head = Node(1,Node(2,Node(3,Node(4,Node(5,Node(6,Node(7)))))))
    self.assertEqual(None, kth_to_last(head, 0));
    self.assertEqual(7, kth_to_last(head, 1).data);
    self.assertEqual(4, kth_to_last(head, 4).data);
    self.assertEqual(2, kth_to_last(head, 6).data);
    self.assertEqual(1, kth_to_last(head, 7).data);

if __name__ == "__main__":
  unittest.main()