#User function Template for python3
 
class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        meets = [(start[i], end[i]) for i in range(n)]
        
        meets.sort(key=lambda x: x[1])
                
        count = 0
        endtime = 0
        
        for meet in meets:
            if meet[0] > endtime:
                count += 1
                endtime = meet[1]
        
        return count


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        start = list(map(int,input().strip().split()))
        end = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.maximumMeetings(n,start,end))
# } Driver Code Ends