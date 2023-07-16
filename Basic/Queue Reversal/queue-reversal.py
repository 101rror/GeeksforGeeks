#User function Template for python3

class Solution:
    #Function to reverse the queue.
    def rev(self, q):
        n = q.maxsize
        ans = []
        
        for i in range(n):
            ans.append(q.get())
        for i in range(n):
            q.put(ans.pop())
        
        return q


#{ 
 # Driver Code Starts

#Initial Template for Python 3

from queue import Queue
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n=int(input())
        a=list(map(int,input().split()))
        q=Queue(maxsize=n)
        for j in a:
            q.put(j)
            
        ob = Solution()
        q=ob.rev(q)
        for i in range(0,n):
            print(q.get(),end=" ")
        print()
# } Driver Code Ends