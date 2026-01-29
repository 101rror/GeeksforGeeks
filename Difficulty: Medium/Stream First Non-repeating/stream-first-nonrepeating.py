from collections import deque

class Solution:
    def firstNonRepeating(self, s):
        freq = [0] * 26
        q = deque()
        ans = []

        for ch in s:
            idx = ord(ch) - ord('a')
            freq[idx] += 1
            q.append(ch)

            while q and freq[ord(q[0]) - ord('a')] > 1:
                q.popleft()
                
            ans.append(q[0]) if q else ans.append('#')


        return ''.join(ans)
