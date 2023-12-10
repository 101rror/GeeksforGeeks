#User function Template for python3

class Solution:
    def subArrayExists(self,arr,n):
        st = set()
        ele = arr[0]
        
        for i in range(1, n):
            st.add(ele)
            ele += arr[i]
            
            if ele == 0 or ele in st:
                return True
                
        return False


#{ 
 # Driver Code Starts
#Initial Template for Python 3



def main():
    T=int(input())
    while(T>0):
        
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        if(Solution().subArrayExists(arr,n)):
            print("Yes")
        else:
            print("No")
        
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends