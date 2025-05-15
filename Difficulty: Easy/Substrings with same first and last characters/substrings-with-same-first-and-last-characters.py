import collections

class Solution:
	def countSubstring(self, s):
		counter = collections.Counter(s)
        count = 0
        
        for ch in counter:
            f = counter[ch]
            count += (f * (f - 1)) // 2
            count += f
            
        return count

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s = input()

        ob = Solution()
        answer = ob.countSubstring(s)

        print(answer)
        print("~")

# } Driver Code Ends