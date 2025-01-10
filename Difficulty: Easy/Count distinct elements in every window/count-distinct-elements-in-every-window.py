
class Solution:
    def countDistinct(self, arr, k):
        n = len(arr)
        unique = []
        
        for i in range(n - k + 1):
            window = len(list(set(arr[i : i + k])))
            unique.append(window)
            
        return unique
#{ 
 # Driver Code Starts
import sys
from collections import defaultdict
if __name__ == '__main__':
    input = sys.stdin.read
    data = input().splitlines()
    t = int(data[0])
    index = 1
    while t > 0:
        arr = list(map(int, data[index].strip().split()))
        index += 1
        k = int(data[index])
        index += 1

        ob = Solution()
        res = ob.countDistinct(arr, k)

        for element in res:
            print(element, end=" ")
        print()
        print("~")

        t -= 1

# } Driver Code Ends