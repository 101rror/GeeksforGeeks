#{ 
 # Driver Code Starts

# } Driver Code Ends
class Solution:
    def sort012(self, arr):
        zero = arr.count(0)
        one = arr.count(1)
        two = arr.count(2)
        
        for i in range(len(arr)):
            arr[i] = 0
            
        for i in range(zero, len(arr)):
            arr[i] = 1
            
        for i in range(zero + one, len(arr)):
            arr[i] = 2
            
        
        return arr
        

#{ 
 # Driver Code Starts.
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
        print("~")
        
if __name__ == "__main__":
    main()

# } Driver Code Ends