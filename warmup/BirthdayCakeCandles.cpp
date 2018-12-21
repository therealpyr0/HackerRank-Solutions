#include <bits/stdc++.h>

using namespace std;

int birthdayCakeCandles(int n, vector <int> ar) {
    // Complete this function
    int i,total=0,max=-1;
    for(i=0;i<n;i++){
        if(ar[i]>max){
            max=ar[i];
            total=1;
            continue;
        }
        if(ar[i]==max)total++;
    }
    return total;

}

int main() {
    int n;
    cin >> n;
    vector<int> ar(n);
    for(int ar_i = 0; ar_i < n; ar_i++){
       cin >> ar[ar_i];
    }
    int result = birthdayCakeCandles(n, ar);
    cout << result << endl;
    return 0;
}
