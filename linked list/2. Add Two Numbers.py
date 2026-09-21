'''2. Add Two Numbers
""Example:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.'''
#code link: https://leetcode.com/problems/add-two-numbers/description/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        r1=""
        r2=""
        while l1 :
            r1+=str(l1.val)
            l1=l1.next
        while l2:
            r2+=str(l2.val)
            l2=l2.next
        b=str(int(r1[::-1])+int(r2[::-1]))
       
        root1=None
        head=None
        l3=[]
        for i in b[::-1]:
            node=ListNode(int(i))
            if head is None:
                head=node
                root1=node
            else:
                root1.next=node
                root1=node
        return head
    
