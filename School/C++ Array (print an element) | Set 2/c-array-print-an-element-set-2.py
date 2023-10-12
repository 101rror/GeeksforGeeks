#User function Template for python3

def findElementAtIndex(arr,n,key):
    for i in range(n):
        if(i == key):
            return arr[i]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t=int(input())
for i in range(t):
    arr=[]
    n, key = map(int, input().split())
    arr = list(map(int, input().split()))
    print(findElementAtIndex(arr,n,key))
# } Driver Code Ends