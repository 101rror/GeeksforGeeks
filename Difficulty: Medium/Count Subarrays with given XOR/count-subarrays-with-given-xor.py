from collections import defaultdict

class Solution:
    def subarrayXor(self, arr, k):
        freq = defaultdict(int)
        xor = 0
        count = 0
        
        for num in arr:
            xor ^= num
            target = xor ^ k
            
            if xor == k:
                count += 1
            if target in freq:
                count += freq[target]
            freq[xor] += 1
            
        return count


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    tc = int(input())

    for _ in range(tc):
        arr = list(map(int, input().split()))
        k = int(input())

        obj = Solution()
        print(obj.subarrayXor(arr, k))
        print("~")

# } Driver Code Ends