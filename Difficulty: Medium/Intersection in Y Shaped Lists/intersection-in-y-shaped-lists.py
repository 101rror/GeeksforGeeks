'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''

class Solution:
    def intersectPoint(self, head1, head2):
        seen = set()
        temp1 = head1
        
        while temp1:
            seen.add(temp1)
            temp1 = temp1.next
            
        temp2 = head2
        while temp2:
            if temp2 in seen:
                return temp2
            temp2 = temp2.next
        
        return -1