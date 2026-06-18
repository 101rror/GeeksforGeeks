class Solution:
    def findCoverage(self, mat):
        m, n = len(mat), len(mat[0])

        def coverage(itr):
            count = 0
            flag = False

            for cell in itr:
                if cell:
                    flag = True
                elif flag:
                    count += 1
            return count

        count = 0

        for row in mat:
            count += coverage(row)
            count += coverage(reversed(row))

        for col in range(n):
            count += coverage(mat[row][col] for row in range(m))
            count += coverage(mat[row][col] for row in reversed(range(m)))

        return count
