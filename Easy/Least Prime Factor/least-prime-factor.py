#User function Template for python3

from math import sqrt

class Solution:
    def least_prime_factor(self, x):
        for i in range(2, int(sqrt(x))+1):
            if (x % i == 0):
                return i
                
        return x
    
    def leastPrimeFactor (self, n):
        result = [1]*(n+1)
        
        for i in range(2, n+1):
            if (i % 2 == 0):                 
                result[i] = 2
            else:
                result[i] = self.least_prime_factor(i)
        return result


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution();
		ans = ob.leastPrimeFactor(n)
		for i in range(1, n+1):
			print(ans[i], end = " ")
		print()

# } Driver Code Ends