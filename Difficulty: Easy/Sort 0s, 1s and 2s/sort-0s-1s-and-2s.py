class Solution:
    def sort012(self, arr):
        def sort(arr):
            low = 0
            mid = 0
            high = len(arr) - 1

            while mid <= high:
                if arr[mid] == 0:
                    arr[low], arr[mid] = arr[mid], arr[low]
                    low += 1
                    mid += 1
                elif arr[mid] == 1:
                    mid += 1
                else:
                    arr[high], arr[mid] = arr[mid], arr[high]
                    high -= 1
                    
        return sort(arr)


#{ 
 # Driver Code Starts
def main():
    t = int(input().strip())  # Read the number of test cases
    ob = Solution()

    while t > 0:
        t -= 1
        arr = list(map(int,
                       input().strip().split())
                   )  # Read the array as space-separated integers
        ob.sort012(arr)  # Sort the array

        print(' '.join(map(str, arr)))  # Print the sorted array


if __name__ == "__main__":
    main()

# } Driver Code Ends