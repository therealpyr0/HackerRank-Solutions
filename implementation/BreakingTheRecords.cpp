#include <bits/stdc++.h>

using namespace std;

vector < int > getRecord(vector < int > s,int n){
    int min,max,maxtotal=0,mintotal=0,i;
    min=s[0];max=s[0];
    for(i=1;i<n;i++){
        if(s[i]>max){maxtotal++;max=s[i];}
        if(s[i]<min){mintotal++;min=s[i];}
    }
    vector<int> ans;
    ans.push_back(maxtotal);
    ans.push_back(mintotal);
    return ans;
    // Complete this function
}

int main() {
    int n;
    cin >> n;
    vector<int> s(n);
    for(int s_i = 0; s_i < n; s_i++){
       cin >> s[s_i];
    }
    vector < int > result = getRecord(s,n);
    string separator = "", delimiter = " ";
    for(auto val: result) {
        cout<<separator<<val;
        separator = delimiter;
    }
    cout<<endl;
    return 0;
}
