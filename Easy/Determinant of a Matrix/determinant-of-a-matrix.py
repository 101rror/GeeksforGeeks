class Solution:
    def determinantOfMatrix(self, mat, n):
        if n == 1:
            return mat[0][0]
        if n == 2:
            return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]
            
        det = 0
        
        for i in range(n):
            ans = [mat[j][1:] for j in range(n) if j != i]
            det += ((-1) ** (i)) * mat[i][0] * self.determinantOfMatrix(ans, n - 1)
            
        return det

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        values = list(map(int, input().strip().split()))
        k = 0
        matrix =[]
        for i in range(n):
            row=[]
            for j in range(n):
                row.append(values[k])
                k+=1
            matrix.append(row)
        obj = Solution()
        print(obj.determinantOfMatrix(matrix,n))
# } Driver Code Ends