class Solution:
    def maxValue(self, arr):
        def rob(arr):
            chosen, notchosen = 0, 0
            for e in arr:
                maxchosen = notchosen + e
                maxnotchosen = max(chosen, notchosen)
                chosen, notchosen = maxchosen, maxnotchosen
            
            return max(chosen, notchosen)
            
        return max(rob(arr[:-1]), rob(arr[1:]))
        



#{ 
 # Driver Code Starts
class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self):
        arr = [int(i) for i in input().strip().split()]
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = IntArray().Input()

        obj = Solution()
        res = obj.maxValue(arr)

        print(res)
        print("~")

# } Driver Code Ends