#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def isStraightHand(self,N, groupSize, hand):
        mp = {}
        for i in hand:
            mp[i] = mp.get(i, 0) + 1
        hand.sort()
        
        for card in hand:
            if not mp[card]:
                continue
            
            for j in range(groupSize):
                curCard = card + j
                if mp.get(curCard, 0) == 0:
                    return False
                mp[curCard] -= 1
        
        return True
        

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N, groupSize = list(map(int, input().split()))
        hand = list(map(int, input().split()))
        ob = Solution()
        res = ob.isStraightHand(N, groupSize, hand);
        print(res)
# } Driver Code Ends