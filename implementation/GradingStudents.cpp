#include <bits/stdc++.h>

using namespace std;

vector < int > solve(vector < int > grades,int n){
    // Complete this function
    int i,rem,diff;
    for(i=0;i<n;i++){
        if(grades[i]<38){continue;}
        rem=grades[i]%5;
        diff=5-rem;
        if(rem>=3){grades[i]+=diff;}
    }
    return grades;
}

int main() {
    int n;
    cin >> n;
    vector<int> grades(n);
    for(int grades_i = 0; grades_i < n; grades_i++){
       cin >> grades[grades_i];
    }
    vector < int > result = solve(grades,n);
    for (ssize_t i = 0; i < result.size(); i++) {
        cout << result[i] << (i != result.size() - 1 ? "\n" : "");
    }
    cout << endl;
    

    return 0;
}
