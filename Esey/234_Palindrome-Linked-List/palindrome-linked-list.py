# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        str_head = ""
        while head:
            str_head += str(head.val)
            head = head.next
        return str_head == str_head[::-1]
