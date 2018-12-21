#include <bits/stdc++.h>

using namespace std;

int migratoryBirds(int n, vector <int> ar) {
    // Complete this function
    int arr[5];
    int i,max=-1,maxindex=0;
    for(i=0;i<5;i++)arr[i]=0;
    for(i=0;i<n;i++){
        arr[ar[i]-1]+=1;
    }
    for(i=0;i<5;i++){
        if(arr[i]>max){
            max=arr[i];
            maxindex=i;
        }
    }
    return maxindex+1;
}

int main() {
    int n;
    cin >> n;
    vector<int> ar(n);
    for(int ar_i = 0; ar_i < n; ar_i++){
       cin >> ar[ar_i];
    }
    int result = migratoryBirds(n, ar);
    cout << result << endl;
    return 0;
}
