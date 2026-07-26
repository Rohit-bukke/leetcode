# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):
        # Initialize tracking pointers
        prev_node = None
        curr_node = head
        
        while curr_node is not None:
            # 1. Temporarily save the next node
            next_node = curr_node.next  
            
            # 2. Reverse the current node's pointer
            curr_node.next = prev_node  
            
            # 3. Move prev_node forward to the current node
            prev_node = curr_node       
            
            # 4. Move curr_node forward to the saved next node
            curr_node = next_node       
            
        # prev_node now points to the new head of the reversed list
        return prev_node

