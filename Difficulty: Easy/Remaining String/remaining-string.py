#User function Template for python3
class Solution:
	def printString(self, s, ch, count):
	    n = len(s)
	    ans = ""
	    c = 0
		
		for x in s:
		    if c == count:
		        break
		    if x == ch:
		        c += 1
		    ans += x
		    
		ln = len(ans)
		newstr = s[ln : n]
		
		return newstr
		        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s = input()
        ch = input()[0]
        count = int(input())
        ob = Solution()
        answer = ob.printString(s, ch, count)

        print(answer)

# } Driver Code Ends