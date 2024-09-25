#User function Template for python3

def displayList(head):
    ans = []
    
    while head:
        ans.append(head.data)
        head = head.next
        
    return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class doublyLL:
    def __init__(self):
        self.head=None

    def insert(self,tail,data):
        head=self.head

        node=Node(data)

        if not head:

            self.head=node
            return node

        tail.next=node
        node.prev=tail
        return node

if __name__=='__main__':
    tcs=int(input())

    for _ in range(tcs):
        n=int(input())
        arr=[int(x) for x in input().split()]

        dll=doublyLL()

        tail=None

        for nodeData in arr:
            tail=dll.insert(tail,nodeData)

        l = displayList(dll.head)
        for x in l:
            print(x,end = ' ')
        print()
        
        for i in range(len(l)-1,-1,-1):
            print(l[i],end = ' ')
        print()

# } Driver Code Ends