#include <bits/stdc++.h>
#define ll long long
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int N;
    ll ans = 0;
    cin >> N;
    vector<int> a(N), b(N);
    for (int i = 0; i < N; i++) cin >> a[i];
    for (int i = 0; i < N; i++) cin >> b[i];
    for (int i = 0; i < N; i++) {
        ans += a[i] * b[i];
    }
    if (ans)
        cout << "No\n";
    else
        cout << "Yes\n";
    return 0;

}
