#User function Template for python3

class Solution:
    def clonestack(self, st, cloned):
        def clone(original, target):
            if not original:
                return
            top = original.pop()
            
            clone(original, target)
            
            target.append(top)
            original.append(top)
            
        clone(st, cloned)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

from collections import deque

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        arr=list(map(int,input().split()))
        
        st=deque()
        copy=[]
        
        for i in range(N):
            st.append(arr[i])
            copy.append(arr[i])
        
        copy = copy[::-1]
            
        cloned=deque()
        
        ob = Solution()
        
        ob.clonestack(st,cloned)
        
        check=[]
        
        while len(cloned):
            check.append(cloned.pop())
        
        flag = 0
        
        if copy != check:
            flag = 1
        
        print(1-flag)
        print("~")
# } Driver Code Ends