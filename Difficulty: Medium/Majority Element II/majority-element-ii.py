from collections import Counter

class Solution:
    def findMajority(self, arr):
        counter = Counter(arr)
        ans = []
        
        n = len(arr)
        t = n // 3
        
        for x, y in counter.items():
            if y > t:
                ans.append(x)
                
        ans.sort()
        
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t = int(input().strip())
    for _ in range(t):
        s = input().strip()
        nums = list(map(int, s.split()))
        ob = Solution()
        ans = ob.findMajority(nums)
        if not ans:
            print("[]")
        else:
            print(" ".join(map(str, ans)))


if __name__ == "__main__":
    main()

# } Driver Code Ends