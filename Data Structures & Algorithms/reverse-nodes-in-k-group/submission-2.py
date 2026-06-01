# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def reverse(begin):
            if not begin:
                return None, None
            end = begin
            for _ in range(k - 1):
                end = end.next
                if not end:
                    return None, None


            newhead = end.next
            node = begin
            lastnode = begin
            while node != end:
                # print(node.val, node.next.val)
                nextnode = node.next
                node.next = newhead
                newhead = node
                node = nextnode

            end.next = newhead
            newhead = end
            return newhead, lastnode


        newhead, lastnode = reverse(head)
        # print(lastnode.val, lastnode.next.val)

        while lastnode:
            oldlastnode = lastnode
            newmid, lastnode = reverse(lastnode.next)
            if newmid:
                oldlastnode.next = newmid
                # print("newmid", newmid.val)

        

        return newhead

        