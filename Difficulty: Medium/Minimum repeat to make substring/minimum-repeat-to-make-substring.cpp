//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
// User function Template for C++

class Solution {
  public:
    int minRepeats(string& s1, string& s2) {
        string s = s1;
        int cnt = 1;
        
        while (s.length() < s2.length()) {
            s += s1;
            cnt++;
        }
        
        if (s.find(s2) != string::npos) return cnt;
    
        s += s1;
        cnt++;
    
        if (s.find(s2) != std::string::npos) return cnt;
    
        return -1;

    }
};

//{ Driver Code Starts.

int main() {
    int t;
    scanf("%d ", &t);
    while (t--) {
        string A, B;
        getline(cin, A);
        getline(cin, B);

        Solution ob;
        cout << ob.minRepeats(A, B) << endl;
    }
    return 0;
}
// } Driver Code Ends