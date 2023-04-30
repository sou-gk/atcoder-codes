#include <iostream>
#include <cmath>
#include <vector>
using namespace std;

vector<long long> gen_primes(int n){
    vector<long long> primes;
    vector<bool> is_prime(n + 1, 1);
    is_prime[0] = is_prime[1] = 0;
    for(int i = 2; i <= n; ++i){
        if(is_prime[i]){
            primes.emplace_back(i);
            for(int j = 2 * i; j <= n; j += i){
                is_prime[j] = 0;
            }
        }
    }
    return primes;
}

int main(){
    long long N;
    cin >> N;
    auto p = gen_primes(sqrt(N / 12));
    int m = p.size(), ans = 0;
    for(int i = 0; i < m; ++i){
        for(int j = i + 1; j < m; ++j){
            for(int k = j + 1; k < m; ++k){
                if(p[i] * p[i] * p[j] > N
                || p[i] * p[i] * p[j] * p[k] > N
                || p[i] * p[i] * p[j] * p[k] * p[k] > N){
                    break;
                }
                ++ans;
            }
        }
    }
    cout << ans << endl;
}
