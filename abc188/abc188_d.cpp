#include <bits/stdc++.h>
#define ll long long
using namespace std;
int dp[100];
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int N, C;
    cin >> N >> C;
    vector<int> a(N), b(N), c(N);
    for (int i = 0; i < N; i++) {
        cin >> a[i] >> b[i] >> c[i];
        for (int j = a[i]; j <= b[i]; j++) {
            dp[j] = min(dp[j] + c[i], C);
        }
    }
    
    
    return 0;

}
