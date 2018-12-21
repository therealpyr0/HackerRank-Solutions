#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    int countvalley=0,count=0;
    int n,i;
    cin>>n;
    char ch;
    for(i=0;i<n;i++){
        cin>>ch;
        if(ch=='U'){
            count++;
            if(count==0){
                countvalley++;
            }
            
        }
        if(ch=='D'){
            count--;
            
        }
    }
    cout<<countvalley;
    return 0;
}
