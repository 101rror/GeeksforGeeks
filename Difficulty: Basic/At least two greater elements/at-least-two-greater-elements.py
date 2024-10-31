#User function Template for python3

class Solution:
    def findElements(self,arr):
        arr.sort()
        
        return arr[:-2]


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while (T > 0):

        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(*ob.findElements(arr))

        T -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends