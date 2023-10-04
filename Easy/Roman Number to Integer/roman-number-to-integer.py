#User function Template for python3

class Solution:
    def romanToDecimal(self, S): 
        roman={'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        n = len(S)
        count = roman[S[n - 1]]
        
        for i in range(n - 1):
            if(roman[S[i]] < roman[S[i + 1]]):
                count -= roman[S[i]]
            else:
                count += roman[S[i]]
                
                
        return count


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for _ in range(t):
        ob = Solution()
        S = input()
        print(ob.romanToDecimal(S))
# } Driver Code Ends