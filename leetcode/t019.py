# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
	#but space cost too high, maybe bad...
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        #push all
        head_lists = []
        while(head):
        	head_lists.append(head)
        	head = head.next
        #if delete origin_head
        if n==len(head_lists):
        	return head_lists[0].next
        #else delete
        to_delete_before = head_lists[len(head_lists)-n-1]
        if to_delete_before.next:
        	to_delete_before.next = to_delete_before.next.next
        else:
        	to_delete_before.next = None
        return head_lists[0]