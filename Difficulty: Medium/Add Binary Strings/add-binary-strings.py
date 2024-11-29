#User function Template for python3
class Solution:
	def addBinary(self, s1, s2):
		ints1 = int(s1, 2)
		ints2 = int(s2, 2)
		ans = ints1 + ints2
		
		return bin(ans).lstrip("0b")


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        a = input().strip()
        b = input().strip()
        ob = Solution()
        answer = ob.addBinary(a, b)

        print(answer)
        print("~")

# } Driver Code Ends