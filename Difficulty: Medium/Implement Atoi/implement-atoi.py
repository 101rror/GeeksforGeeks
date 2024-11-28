#User function template for Python
class Solution:
    def myAtoi(self, s):
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
    
        i, n = 0, len(s)
        ans, sign = 0, 1
    
        while i < n and s[i] == ' ':
            i += 1
    
        if i < n and (s[i] == '+' or s[i] == '-'):
            sign = -1 if s[i] == '-' else 1
            i += 1
    
        while i < n and s[i].isdigit():
            digit = int(s[i])
            if ans > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN
    
            ans = ans * 10 + digit
            i += 1
    
        return sign * ans


#{ 
 # Driver Code Starts
#Initial template for Python

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = input()
        ob = Solution()
        print(ob.myAtoi(s))
        print("~")

# } Driver Code Ends