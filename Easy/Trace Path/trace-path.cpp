//{ Driver Code Starts
//Initial Template for C++

#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
//User function Template for C++

class Solution{
public:
    int isPossible(int n, int m, string s){

        int row=0,col=0;
        int maxn =0,minn=0;
        int maxm =0,minm=0;
        for(int i=0;i<s.size();i++)
        {
            char c = s[i];
            if(c=='R')
            {
                col++;
                maxm = max(maxm,col);
            
            }
            else if(c=='L')
            {
                col--;
                minm = min(minm,col);
            }
            else if(c=='D')
            {
                row--;
                minn = min(minn,row);
            }
            else if(c=='U')
            {
                row++;
                maxn = max(maxn,row);
            }
        }
       
        if(maxm-minm>=m || maxn-minn>=n)
        {
            return 0;
        }
        return 1;
    }
};

//{ Driver Code Starts.

int main(){
    int t;
    cin>>t;
    while(t--){
        int n, m;
        cin>>n>>m;
        string s;
        cin>>s;
        
        Solution ob;
        cout<<ob.isPossible(n, m, s)<<endl;
    }
    return 0;
}
// } Driver Code Ends