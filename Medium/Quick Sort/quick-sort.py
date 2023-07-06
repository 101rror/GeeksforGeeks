#User function Template for python3

class Solution:
    def quickSort(self, arr, low, high):
        if (low < high):
            mid = self.partition(arr, low, high)
            self.quickSort(arr, low, mid - 1)
            self.quickSort(arr, mid + 1, high)

    def partition(self, arr, low, high):
        pos = low
        pivot = arr[low]
        
        while (low <= high):
            while (low <= high and arr[low] <= pivot):
                low += 1
            while (low <= high and arr[high] > pivot):
                high -= 1
                
            if (low <= high):
                arr[low], arr[high] = arr[high], arr[low]
            if (low > high):
                break
            
        arr[pos], arr[high] = arr[high], arr[pos]
        
        return high


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        Solution().quickSort(arr,0,n-1)
        for i in range(n):
            print(arr[i],end=" ")
        print()

# } Driver Code Ends