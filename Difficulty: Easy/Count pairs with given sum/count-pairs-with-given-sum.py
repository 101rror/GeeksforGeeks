#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


# } Driver Code Ends
#User function Template for python3
from collections import defaultdict

class Solution:
    def countPairs(self,arr, target):
        count = 0
        freq = defaultdict(int)
        
        for num in arr:
            x = target - num
            if x in freq:
                count += freq[x]
                
            freq[num] += 1
                    
        return count
        
        
        

#{ 
 # Driver Code Starts.

def main():
    T = int(input())
    while (T > 0):

        A = [int(x) for x in input().strip().split()]

        k = int(input())
        ob = Solution()
        print(ob.countPairs(A, k))
        print('~')
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends