#User function Template for python3

def rotate(mat):
    n = len(mat)
    
    for i in range(n):
        for j in range(i + 1, len(mat)):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
    
    for i in range(n):
        mat[i] = mat[i][::-1]
        
    
    return mat


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        matrix = []
        for i in range(N):
            arr = [int(x) for x in input().strip().split()]
            matrix.append(arr)

        rotate(matrix)
        for i in range(N):
            for j in range(N):
                print(matrix[i][j], end=' ')
            print()
        print("~")

# } Driver Code Ends