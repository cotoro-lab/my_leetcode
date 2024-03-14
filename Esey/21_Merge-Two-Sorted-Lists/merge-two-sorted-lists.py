# 21. Merge Two Sorted Lists
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def listnode_to_list(self, listnode):
        list = []
        while listnode:
            list.append(listnode.val)
            listnode = listnode.next
        return list

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        sort_array = self.listnode_to_list(list1) + self.listnode_to_list(list2)
        sort_array.sort()

        # Convert sorted array to ListNode
        dummy = ListNode(0)
        ptr = dummy
        for i in sort_array:
            ptr.next = ListNode(i)
            ptr = ptr.next

        return dummy.next


