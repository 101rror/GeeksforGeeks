class Solution:
    def kSubstr(self, s: str, k: int) -> bool:
        n = len(s)
        freq = {}

        for i in range(0 , n , k):
            sub = s[i : i + k]

            freq[sub] = freq.get(sub , 0) + 1

        if len(freq) == 1:
            return True

        if len(freq) == 2:
            for sub in freq:
                if freq[sub] == 1:
                    return True

        return False
