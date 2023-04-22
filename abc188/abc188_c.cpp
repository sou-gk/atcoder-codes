#include <bits/stdc++.h>
#define ll long long
#define pii pair<int,int>
using namespace std;
const int maxn = 2e5;
int a[maxn];
int N;

int func (int i) {
    if (a[i])   return a[i];
    if (i == 1)
        a[i] = min(func(2 * i), func(2 * i + 1));
    else
        a[i] = max(func(2 * i), func(2 * i + 1));
    return a[i];
}

int main() {
    // ios::sync_with_stdio(0);
    // cin.tie(0);
    memset(a, 0, sizeof(a));
    cin >> N;
    int num = pow(2, N);
    for (int i = num; i < num * 2; i++)  cin >> a[i];

    int f = func(1), ans = 0;
    for (int i = num; i < num * 2; i++)
        if (a[i] == f) {
            ans = i - num + 1;
            break;
        }
    cout << ans << '\n';
    return 0;

}
