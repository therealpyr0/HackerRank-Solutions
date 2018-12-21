#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <climits>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    vector<int> v,ans;
    int n,i,num,min=INT_MAX;
    
    cin>>n;
    for(i=0;i<n;i++){
        cin>>num;
        v.push_back(num);
    }
    sort(v.begin(),v.end());
    int diff;
    for(i=0;i<n-1;i++){
        diff=v[i+1]-v[i];
        diff=abs(diff);
        if(diff<min){
            min=diff;
            //cout<<v[i]<<" "<<v[i+1];
            ans.clear();
            ans.push_back(v[i]);
            ans.push_back(v[i+1]);
            continue;
        }
        if(diff==min){
            ans.push_back(v[i]);
            ans.push_back(v[i+1]);
        }
    }
    for(i=0;i<ans.size();i++){
        cout<<ans[i]<<" ";
    }
    return 0;
}
