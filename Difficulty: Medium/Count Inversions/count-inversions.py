class Solution:
    def inversionCount(self, arr):
        temp = [0]*len(arr)
        
        def split(arr, i, j):
            inversions = 0
            if i < j:
                m = (i+j)//2
                inversions += split(arr, i, m)
                inversions += split(arr, m+1, j)
                inversions += merge(arr, i, m, j)
            return inversions
                
        def merge(arr, i, m, j):
            p1 = i
            p2 = m+1
            pt = i
            inversions = 0
            while p1 <= m and p2 <= j:
                if arr[p1] <= arr[p2]:
                    temp[pt] = arr[p1]
                    pt += 1
                    p1 += 1
                else:
                    temp[pt] = arr[p2]
                    inversions += (m - p1 + 1)
                    pt += 1
                    p2 += 1
            while p1 <= m:
                temp[pt] = arr[p1]
                p1 += 1
                pt += 1
            while p2 <= j:
                temp[pt] = arr[p2]
                p2 += 1
                pt += 1
            arr[i:j+1] = temp[i:j+1]
            return inversions
            
        return split(arr, 0, len(arr)-1)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        a = list(map(int, input().strip().split()))
        obj = Solution()
        print(obj.inversionCount(a))
        print("~")

# } Driver Code Ends