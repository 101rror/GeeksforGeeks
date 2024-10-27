#User function Template for python3

class MyQueue:
    def __init__(self):
        self.queue = []
        
    def push(self, x):
        self.queue.append(x)
        
    def pop(self): 
        if len(self.queue) == 0:
            return -1
        
        ele = self.queue[0]
        self.queue.pop(0)
        
        return ele


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for i in range(t):
        s=MyQueue()
        q=int(input())
        q1=list(map(int,input().split()))
        i=0
        while(i<len(q1)):
            if(q1[i]==1):
                s.push(q1[i+1])
                i=i+2
            elif(q1[i]==2):
                print(s.pop(),end=" ")
                i=i+1
            elif(s.isEmpty()):
                print(-1)
                i=i+1
        print()   

        print("~")
# } Driver Code Ends