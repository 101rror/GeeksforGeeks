#User function template for Python 3
from collections import Counter

class Solution:
    def majorityElement(self, arr):
        n = len(arr)
        t = n // 2
        
        counter = Counter(arr)
        
        for x, y in counter.items():
            if y > t:
                return x
                
        return -1
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

from sys import stdin


def main():
    T = int(input())
    while (T > 0):

        A = [int(x) for x in input().strip().split()]

        obj = Solution()
        print(obj.majorityElement(A))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends