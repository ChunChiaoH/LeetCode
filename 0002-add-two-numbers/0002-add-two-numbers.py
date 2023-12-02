# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # create another ListNode for sum
        new_node = ListNode(0, None)
        cur_node = new_node
        # the value to add to next bit
        add_to_next = 0
        
        # iterate until both l1 and l2 are exhausted
        while l1 or l2:
            l2v = l2.val if l2 else 0
            l1v = l1.val if l1 else 0
            # sum of l1 and l2
            add_to_cur = (l1v + l2v + cur_node.val)%10
            add_to_next = (l1v + l2v + cur_node.val)//10
            
            cur_node.val = add_to_cur
            # cur_node.val may be one or zero depending on previous loop
            #cur_node.val += add_to_cur
            #cur_node.val += (cur_node.val + add_to_cur) % 10
            #add_to_next += cur_node.val//10
            #cur_node.val = cur_node.val%10
            if (l1 and l1.next) or (l2 and l2.next):
                cur_node.next = ListNode(add_to_next, None)
            else:
                cur_node.next = None
            l1 = l1.next if l1 and l1.next != None else None 
            l2 = l2.next if l2 and l2.next != None else None
            cur_node = cur_node.next if cur_node.next else cur_node
        if add_to_next:
            cur_node.next = ListNode(add_to_next, None)
        return new_node