# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        start_prev = None
        start = None
        end = None
        node = head

        while node:
            left -= 1
            right -= 1
            if left == 1:
                start_prev = node
            if left == 0:
                start = node
            if right == 0:
                end = node
            node = node.next

        """
        while node:
            if not start and node.val >= left:
                start = node
                continue
            if start and node.val <= right:
                end = node
            if node.val > right:
                break
            if not start:
                start_prev = node
            node = node.next
        """
        # print(start.val, end.val)

        if start == head:
            # print("start is head")
            head = end

        end_nxt = end.next
        prev = end.next
        end.next = None
        node = start
        while node and node != end_nxt:
            nxt = node.next
            node.next = prev
            prev = node
            node = nxt

        if start_prev:
            start_prev.next = end
        
        # self.print(head)

        return head

    
    def print(self, node):
        vals = list()
        while node:
            vals.append(str(node.val))
            node = node.next
        print("-".join(vals))

        
        