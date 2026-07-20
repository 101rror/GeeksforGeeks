class Solution:
    def findPrefixes(self, arr):
        n = len(arr)
        root = {"count": n}
        
        for word in arr:
            trie = root
            for c in word:
                if c in trie:
                    trie = trie[c]
                    trie["count"] += 1
                else:
                    trie[c] = trie = {"count": 1}
                    
        ans = []
        
        for word in arr:
            trie = root
            for i in range(len(word)):
                trie = trie[word[i]]
                if trie["count"] == 1:
                    ans.append(word[:i + 1])
                    break
            else:
                ans.append(word)
                
        return ans
        