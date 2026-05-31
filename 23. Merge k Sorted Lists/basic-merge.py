# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        for i in reversed(range(len(lists))):
            if lists[i] is None:
                lists.pop(i)
        if len(lists) == 0:
            return None
        sorted_list_wrapper = ListNode()
        last_node = sorted_list_wrapper
        while lists:
            last_node.next = ListNode()
            last_node = last_node.next
            min_list_head_index = None
            min_list_head = 10**4 + 1
            for i in range(len(lists)):
                if lists[i].val < min_list_head:
                    min_list_head = lists[i].val
                    min_list_head_index = i
            last_node.val = min_list_head
            lists[min_list_head_index] = lists[min_list_head_index].next
            if lists[min_list_head_index] is None:
                lists.pop(min_list_head_index)
        last_node = None
        return sorted_list_wrapper.next
                
