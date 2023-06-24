#User function Template for python3

class Solution:
    def klengthpref(self, arr, n, k, s):
        ln = len(s)
        count = 0
        
        if (k > ln):
            return 0

        for i in range(n):
            string = arr[i]
            if string[:k] == s[:k]:
                count += 1
                
        return count
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == "__main__":
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr = []
        for x in range(n):
            s1 = input()
            arr.append(s1)
        k = int(input())
        s = input()
        obj = Solution()
        print(obj.klengthpref(arr,n,k,s))
        
        
# } Driver Code Ends