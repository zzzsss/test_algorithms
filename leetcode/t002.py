# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ret = ListNode(0)	#first node is the starter node
        assign = ret
        carry = 0
        #1:while both l1 and l2 have numbers
        while l1 and l2:
        	assign.next = ListNode(0)
        	assign = assign.next
       		assign.val = (l1.val+l2.val+carry)%10
       		carry = (l1.val+l2.val+carry)/10
       		l1 = l1.next
       		l2 = l2.next
       	#2: remains
       	rema = l1
       	if not rema:
       		rema = l2
       	while rema:
        	assign.next = ListNode(0)
        	assign = assign.next
       		assign.val = (rema.val+carry)%10
       		carry = (rema.val+carry)/10
       		rema = rema.next
       	#3: carry
       	if carry:
       		assign.next = ListNode(1)
       	return ret.next
       	  