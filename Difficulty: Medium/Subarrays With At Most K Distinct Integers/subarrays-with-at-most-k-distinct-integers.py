class Solution:
    def countAtMostK(self, arr, k):
        n = len(arr)
        
        if k == 0:
            return 0

        freq = {}
        left, uniq, count = 0, 0, 0

        for right in range(n):
            if arr[right] not in freq or freq[arr[right]] == 0:
                uniq += 1
                
            freq[arr[right]] = freq.get(arr[right], 0) + 1

            while uniq > k:
                freq[arr[left]] -= 1
                if freq[arr[left]] == 0:
                    uniq -= 1
                left += 1

            count += (right - left + 1)

        return count