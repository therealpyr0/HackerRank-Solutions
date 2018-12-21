#include <bits/stdc++.h>
#include <limits>
using namespace std;

int main(){
    int n,i,min=INT_MAX,diff;
    cin >> n;
    vector<int> a(n);
    for(int a_i = 0; a_i < n; a_i++){
       cin >> a[a_i];
    }
    sort(a.begin(),a.end());
    for(i=0;i<n-1;i++){
        diff=abs(a[i]-a[i+1]);
        if(diff<=min)min=diff;
        //cout<<"diff : "<<a[i]<<" "<<a[i+1]<<" "<<diff<<endl;
    }
    cout<<min;
    // your code goes here
    return 0;
}
