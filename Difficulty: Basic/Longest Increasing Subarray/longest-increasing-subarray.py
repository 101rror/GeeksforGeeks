#User function Template for python3

class Solution:
    def lenOfLongIncSubArr(self, arr):
        mx = 1
        count = 1
        
        for i in range(1, len(arr)):
            if arr[i] > arr[i - 1]:
                count += 1
            else:
                mx = max(mx, count)
                count = 1
                
        mx = max(mx, count)
                
        return mx
    
    
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')

    t = int(data[0])
    results = []

    for i in range(1, t + 1):
        arr = list(map(int, data[i].split()))
        solution = Solution()
        ans = solution.lenOfLongIncSubArr(arr)
        results.append(ans)

    for result in results:
        print(result)
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends