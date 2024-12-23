
#User function Template for python3

class Solution:
    
    #Function to search a given number in row-column sorted matrix.
    def searchRowMatrix(self, mat, x): 
    	n, m = len(mat), len(mat[0])
    	
    	for i in range(n):
    	    first, last = 0, m - 1
    	    
    	    if mat[i][first] > x or mat[i][last] < x:
    	        continue 
    	    while first <= last:
    	        mid = (first + last) // 2
    	        if mat[i][mid] == x:
    	            return True
    	        elif mat[i][mid] < x:
    	            first = mid + 1
    	        else:
    	            last = mid - 1
    	            
    	return False
    	



#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()

    t = int(data[0])
    index = 1
    for _ in range(t):
        r = int(data[index])
        c = int(data[index + 1])
        index += 2
        matrix = []
        for i in range(r):
            row = list(map(int, data[index:index + c]))
            matrix.append(row)
            index += c
        x = int(data[index])
        index += 1
        ob = Solution()
        if ob.searchRowMatrix(matrix, x):
            print("true")
        else:
            print("false")
        print("~")
# } Driver Code Ends