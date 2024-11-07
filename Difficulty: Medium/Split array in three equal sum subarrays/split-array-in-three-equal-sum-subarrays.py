#User function Template for python3
class Solution:
    def findSplit(self,arr):
        total_sum = sum(arr)
        if total_sum % 3 != 0:
            return [-1, -1]
            
        part_sum = total_sum // 3
        n = len(arr)
        current_sum = 0
        i, j = -1, -1
        
        for index in range(n):
            current_sum += arr[index]
            if current_sum == part_sum:
                i = index
                break
            
        if i == -1:
            return [-1, -1]
            
        current_sum = 0
        for index in range(i + 1, n):
            current_sum += arr[index]
            if current_sum == part_sum:
                j = index
                break
            
        if j == -1 or j == n - 1:
            return [-1, -1]
            
        return [i, j]

#{ 
 # Driver Code Starts
# Initial Template for Python 3

# Main
if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        arr = [int(x) for x in input().strip().split()]

        ob = Solution()
        result = ob.findSplit(arr)

        if (result == [-1, -1]) or len(result) != 2:
            print("false")
        else:
            sum1 = sum2 = sum3 = 0
            for i in range(len(arr)):
                if i <= result[0]:
                    sum1 += arr[i]
                elif i <= result[1]:
                    sum2 += arr[i]
                else:
                    sum3 += arr[i]

            if sum1 == sum2 == sum3:
                print("true")
            else:
                print("false")
        print("~")

# } Driver Code Ends