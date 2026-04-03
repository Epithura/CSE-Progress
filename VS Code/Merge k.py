from typing import List, Optional

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def ith_element(head: ListNode, i):
            current = head
            index = 0
            while current:
                if index == i:
                    return current.val
                current = current.next
                index += 1
            raise IndexError("Index out of range")

        def length_of_listnode(head: ListNode):
            count = 0
            current = head
            while current:
                count += 1
                current = current.next
            return count

        def merge_sorted(L1, L2):
            i = 0
            j = 0
            dummy = ListNode(0)
            current = dummy
            while i < length_of_listnode(L1) and j < length_of_listnode(L2):
                if ith_element(L1, i) <= ith_element(L2, j):
                    current.next = ListNode(ith_element(L1, i))
                    i += 1
                else:
                    current.next = ListNode(ith_element(L2, j))
                    j += 1
                current = current.next

            if i == length_of_listnode(L1):
                for k in range(j, length_of_listnode(L2)):
                    current.next = ListNode(ith_element(L2, k))
                    current = current.next
            elif j == length_of_listnode(L2):
                for k in range(i, length_of_listnode(L1)):
                    current.next = ListNode(ith_element(L1, k))
                    current = current.next

            return dummy.next
        for i in range(len(lists)-1):
            lists[i+1]=merge_sorted(lists[i],lists[i+1])
        return lists[-1]