class Solution:
    def spirallyTraverse(self, mat):
        row = len(mat)
        col = len(mat[0])
        ans = []
        
        top, bottom = 0, row - 1
        left, right = 0, col - 1
        
        while top <= bottom and left <= right:
            for i in range(left, right + 1):
                ans.append(mat[top][i])
            top += 1
            
            for i in range(top, bottom + 1):
                ans.append(mat[i][right])
            right -= 1
            
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    ans.append(mat[bottom][i])
                bottom -= 1
                
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    ans.append(mat[i][left])
                left += 1
                
        return ans
            
            


#{ 
 # Driver Code Starts
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

        solution = Solution()
        result = solution.spirallyTraverse(matrix)
        print(" ".join(map(str, result)))
        print("~")

# } Driver Code Ends