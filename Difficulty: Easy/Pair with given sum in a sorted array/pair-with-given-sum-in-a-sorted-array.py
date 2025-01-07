#User function Template for python3


class Solution:
    def countPairs (self, arr, target) : 
        n = len(arr)
        count = 0
        freq = {}
        
        for num in arr:
            check = target - num
            if check in freq:
                count += freq[check]
            
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
                
        return count
#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    import sys
    input = sys.stdin.read
    data = input().split('\n')

    t = int(data[0].strip())
    index = 1

    for _ in range(t):
        arr = list(map(int, data[index].strip().split()))
        index += 1
        target = int(data[index].strip())
        index += 1

        res = Solution().countPairs(arr, target)
        print(res)
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends