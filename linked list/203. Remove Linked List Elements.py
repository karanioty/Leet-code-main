'''203. Remove Linked List Elements
""Example:
Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]'''
#code link: https://leetcode.com/problems/remove-linked-list-elements/description/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode | None, val: int) -> ListNode | None:
        temp1=ListNode(0)
        temp1.next=head
        temp=temp1

        while temp.next:
            if temp.next.val==val:
                temp.next=temp.next.next
            else:
                temp=temp.next
        return temp1.next
