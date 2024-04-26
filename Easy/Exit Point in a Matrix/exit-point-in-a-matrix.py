#User function Template for python3

class Solution:
	def FindExitPoint(self, n, m, mat):
	    x = y = 0
	    flag = 0
	    while x >= 0 and y >= 0 and x < n and y < m:
	        if mat[x][y] == 1:
	            flag = (flag + 1) % 4
	            mat[x][y] = 0
	        if flag == 0:
	            y += 1
	        elif flag == 1:
	            x += 1
	        elif flag == 2:
	            y -= 1
	        else:
	            x -= 1
	    
	    return max(min(x, n-1), 0), max(min(y, m-1), 0)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n, m = input().split()
        n = int(n)
        m = int(m)
        matrix = []
        for _ in range(n):
            matrix.append(list(map(int, input().split())))
        ob = Solution()
        ans = ob.FindExitPoint(n, m, matrix)
        for _ in ans:
            print(_, end=" ")
        print()

# } Driver Code Ends