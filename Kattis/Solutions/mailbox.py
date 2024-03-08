#include <bits/stdc++.h>
#define ll long long
using namespace std;
int dp[11][101][101];
int g(ll k, ll start, ll end){
    if(dp[k][start][end]!=-1){ //if found return
        return dp[k][start][end];
    }
    else if(start==end){//takes 0 crackers
        return 0;
    }
    else if(k==0){ // need infinite crackers if no boxes
        return INT_MAX;
    }
    ll mini = INT_MAX;
    for(ll i = start+1;i<=end;i++){
        mini = min(mini,i+max(g(k,i,end),g(k-1,start,i-1)));
    }
    dp[k][start][end]=mini;
    return mini;
}
void solve(){
    ll k,m;
    cin >> k >> m;
    memset(dp,-1,sizeof dp);//reset dp array so i dont need to use vectors
    cout << g(k,0,m) << endl; //min # of crackers needed such that we can find
    //the smallest number between start and end that the box explodes where it explodes at end+1

}

int main() {
    ll t;
    cin >> t;
    while(t--){
    solve();
    }


    return 0;
}