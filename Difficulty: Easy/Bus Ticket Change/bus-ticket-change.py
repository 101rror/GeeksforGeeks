class Solution:
    def canServe(self, arr):
        five = 0
        ten = 0

        for num in arr:
            if num == 5:
                five += 1
            elif num == 10:
                if five == 0:
                    return False
                five -= 1
                ten += 1
            else:
                if ten > 0 and five > 0:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False

        return True