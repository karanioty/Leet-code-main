'''23. Merge k Sorted Lists
""Example:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted linked list:
1->1->2->3->4->4->5->6'''
#code link: https://leetcode.com/problems/merge-k-sorted-lists/description/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        l=[]
        for i in lists:
            print(i)
            while i:
                l.append(i.val)
                i=i.next
        l.sort()
        head=None
        tail=None
        for i in l:
            root= ListNode(i)
            if head is None:
                head=root
                tail=root
            else:
            
                tail.next=root
                tail=root
        return head

            
