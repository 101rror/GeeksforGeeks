'''
Structure of linked list node
class Node:
    def __init__(self,x):
        self.data=x
        self.next=None

'''
class Solution:
    def compute(self,head):
        def reverse(head):
            prev = None
            curr = head
            
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
                
            return prev
        
        head = reverse(head)
        
        mx = head.data
        curr = head
        
        while curr and curr.next:
            if curr.next.data < mx:
                curr.next = curr.next.next
            else:
                curr = curr.next
                mx = curr.data
        
        return reverse(head)
        