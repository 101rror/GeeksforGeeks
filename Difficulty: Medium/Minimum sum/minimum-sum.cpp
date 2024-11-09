//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
// User function template for C++

class Solution {
  public:
    string minSum(vector<int> &arr) {
        // code here
        int n = arr.size();
        sort(arr.begin(),arr.end());
        
        int d = 0, x = 0;
        
        string n1 = "";
        string n2 = "";
        string ans = "";
        
        for(int i = n - 1; i >= 0; i -= 2){
            int cur = arr[i] + arr[i - 1] + x;
            d = cur % 10;
            ans += to_string(d);
            x = cur / 10;
        }
        if(x > 0){
            ans += to_string(x);
        }
        
        reverse(ans.begin(),ans.end());
        int i = 0;
        
        while(ans[i] == '0'){
            i++;
        }
        return ans.substr(i);
        
    }
};

//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    cin.ignore();
    while (t--) {
        vector<int> a;
        string input;
        getline(cin, input);
        stringstream ss(input);
        int number;
        while (ss >> number) {
            a.push_back(number);
        }

        Solution ob;
        string ans = ob.minSum(a);
        cout << ans << endl;
        cout << "~" << endl;
    }
    return 0;
}

// } Driver Code Ends