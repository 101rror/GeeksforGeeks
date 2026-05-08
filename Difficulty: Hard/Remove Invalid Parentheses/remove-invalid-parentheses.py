from collections import deque

class Solution:
    def validParenthesis(self, s):

        def isValid(st):
            cnt = 0

            for ch in st:
                if ch == '(':
                    cnt += 1
                elif ch == ')':
                    cnt -= 1

                if cnt < 0:
                    return False

            return cnt == 0

        q = deque([s])
        visited = {s}

        ans = []

        while q:

            size = len(q)
            found = False

            for _ in range(size):

                curr = q.popleft()

                if isValid(curr):
                    ans.append(curr)
                    found = True

                if found:
                    continue

                for i in range(len(curr)):

                    if curr[i] not in '()':
                        continue

                    nxt = curr[:i] + curr[i + 1:]

                    if nxt not in visited:
                        visited.add(nxt)
                        q.append(nxt)

            if found:
                return sorted(ans)

        return [""]
        