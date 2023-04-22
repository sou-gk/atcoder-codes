#include <bits/stdc++.h>
#define fs first
#define sc second
using namespace std;
typedef pair<int, int> pii;
const int maxn = 1e4 + 10;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int a, b, aa = 0, bb = 0;
    cin >> a >> b;
    while (a) {
        aa += a % 10;
        a /= 10;
    }
    while (b) {
        bb += b % 10;
        b /= 10;
    }
    cout << max(aa, bb) << '\n';
    return 0;
}
