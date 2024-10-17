#User function Template for python3
'''
class Node:
    def _init_(self, data):
        self.data = data
        self.next = None

'''

class Solution:
    def alternatingSplitList(self, head):
        temp = head
        data1 = cur1 = Node(0)
        data2 = cur2 = Node(0)
        idx = 1
        
        while temp:
            if idx % 2 != 0:
                cur1.next = temp
                cur1 = cur1.next
                temp1 = cur1
            else:
                cur2.next = temp
                cur2 = cur2.next
                temp2 = cur2
                
            idx += 1
            temp = temp.next
            
        temp1.next = None
        temp2.next = None
        
        return [data1.next, data2.next]
                
                
        


#{ 
 # Driver Code Starts
class Node:

    def __init__(self, x):
        self.data = x
        self.next = None


def printList(node):
    while node is not None:
        print(node.data, end=" ")
        node = node.next
    print()


if __name__ == "__main__":
    t = int(input().strip())

    for _ in range(t):
        arr = list(map(int, input().strip().split()))

        head = Node(arr[0])
        tail = head

        for i in range(1, len(arr)):
            tail.next = Node(arr[i])
            tail = tail.next

        ob = Solution()
        result = ob.alternatingSplitList(head)
        printList(result[0])
        printList(result[1])

# } Driver Code Ends