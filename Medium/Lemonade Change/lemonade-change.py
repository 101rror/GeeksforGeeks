#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def lemonadeChange(self, N, bills):
        k = []
        
        if bills[0] != 5 :
            return 'False'
            raise SystemExit
            
        for i in bills :
            k.append(i)
            
            if (i == 10) :
                if 5 in k :
                    k.remove(5)
                else :
                    return 'False'
                    raise SystemExit
                    
            if (i == 20) :
                if ((10 in k) and (5 in k)) :
                    k.remove(10)
                    k.remove(5)
                elif (i == 20) and ((5 in k)) :
                    k.remove(5)
                    if 5 in k :
                        k.remove(5)
                    if 5 in k :
                        k.remove(5)
                    else :
                        return 'False'
                        raise SystemExit
                        
                else :
                    return 'False'
                    raise SystemExit
                    
        return 'True'
        

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N = int(input())
        bills = list(map(int, input().split()))
        ob = Solution()
        res = ob.lemonadeChange(N, bills)
        print(res)
# } Driver Code Ends