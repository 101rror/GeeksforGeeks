
class Solution:
    def countTriplets(self, arr, target):
        n = len(arr)
        count = 0

        for i in range(n - 2):
            j, k = i + 1, n - 1

            while j < k:
                check = arr[i] + arr[j] + arr[k]

                if check == target:
                    if arr[j] == arr[k]:
                        comb = (k - j + 1) * (k - j) // 2
                        count += comb
                        break
                    else:
                        left, right = 1, 1

                        while j + 1 < k and arr[j] == arr[j + 1]:
                            left += 1
                            j += 1

                        while k - 1 > j and arr[k] == arr[k - 1]:
                            right += 1
                            k -= 1

                        count += left * right
                        
                        j += 1
                        k -= 1
                elif check < target:
                    j += 1
                else:
                    k -= 1

        return count
#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        target = int(input())
        ob = Solution()
        ans = ob.countTriplets(arr, target)
        print(ans)
        print("~")
# } Driver Code Ends