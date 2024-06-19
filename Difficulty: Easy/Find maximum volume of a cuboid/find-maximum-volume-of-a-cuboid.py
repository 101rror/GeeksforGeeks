#User function Template for python3

class Solution:
    def maxVolume(self, p, a):
        length = (p - math.sqrt(p * p - 24 * a)) / 12
        height = (p / 4) - 2 * length 
        
        ans = length * length * height
        
        return round(ans, 2)


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import math
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        perimeter, area = [int(x) for x in input().split()]

        ob = Solution()
        print('%.2f' % ob.maxVolume(perimeter, area))

# } Driver Code Ends