# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        sum1=0
        sum2=0
        den=1
        while l1:
            sum1+=l1.val*den
            den*=10
            l1=l1.next
        den=1
        while l2:
            sum2+=l2.val*den
            den*=10
            l2=l2.next
        sum=sum1+sum2
        result_start=ListNode(sum%10)
        result=result_start
        if sum<10:
            return result_start
        while True:
            sum/=10
            result.next=ListNode(sum%10)
            result=result.next
            if sum<10:
                return result_start
            
        
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        