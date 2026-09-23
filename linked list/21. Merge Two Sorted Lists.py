'''21. Merge Two Sorted Lists
""Example:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
'''
#code link: https://leetcode.com/problems/merge-two-sorted-lists/description/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        l=[]
        while list1:
            l.append(list1.val)
            list1=list1.next
        while list2:
            l.append(list2.val)
            list2=list2.next
        
        l.sort()
        head=None
        tail=None
        for i in l:
            node=ListNode(i)
            if head is None:
                head=node
                tail=node
            else:
                tail.next=node
                tail=node
        return head
