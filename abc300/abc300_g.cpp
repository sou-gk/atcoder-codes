#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

vector<long long> primes;
vector<bool> is_prime;
int gen_primes(int n){
    is_prime.resize(n + 1, 1);
    is_prime[0] = is_prime[1] = 0;
    for(int i = 2; i <= n; ++i){
        if(is_prime[i]){
            primes.emplace_back(i);
            for(int j = 2 * i; j <= n; j += i){
                is_prime[j] = 0;
            }
        }
    }
    return primes.size();
}

long long N, P, S;
vector<long long> s;
long long dfs(long long v, int i, int mode){
    long long ret = 0;
    if(mode == 0 && i == S){
        s.emplace_back(v);
    }else if(mode == 1 && i == primes.size()){
        ret = upper_bound(s.begin(), s.end(), N / v) - s.begin();
    }else{
        while(v <= N){
            ret += dfs(v, i + 1, mode);
            v *= primes[i];
        }
    }
    return ret;
}

int main(){
    cin >> N >> P;
    S = min(8, gen_primes(P));
    dfs(1, 0, 0);
    sort(s.begin(), s.end());
    cout << dfs(1, S, 1) << endl;
}
