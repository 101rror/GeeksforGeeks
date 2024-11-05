# Function should return an integer value
class Solution:
    def convertFive(self, n):
        if n == 0:
            return 5
        num = 0
        x = 1
        
        while n:
            rem = n % 10
            n //= 10
            if rem == 0:
                rem = 5
                
            num += rem * x
            x *= 10
            
        return num


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        ob = Solution()
        print(ob.convertFive(int(input().strip())))
        print("~")
# } Driver Code Ends