'''206. Reverse Linked List
""Example:

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]'''
#code link: https://leetcode.com/problems/reverse-linked-list/description/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=None
        temp=head
        while temp:
            next_node=temp.next
            temp.next=prev
            prev=temp
            temp=next_node
        return prev
