class Solution:
    def findIndex(self, s):
        clos = s.count(')')
        opn = 0

        for i, ch in enumerate(s):
            if opn == clos:
                return i

            if ch == '(':
                opn += 1
            else:
                clos -= 1

        return len(s)