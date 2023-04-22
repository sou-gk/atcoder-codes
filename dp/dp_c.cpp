#include <bits/stdc++.h>

using namespace std;

int main()
{
  int N;
  cin>>N;
  vector<int> swim;
  vector<int> bugs;
  vector<int> homework;

  for(int i=0; i<N; i++) {
    int a,b,c;
    cin>>a>>b>>c;
    swim.push_back(a);
    bugs.push_back(b);
    homework.push_back(c);
  }

  int dp[N][3];

  for(int i=0; i<N; i++) {
    for(int j=0; j<3; j++) {
      dp[i][j] = 0;
    }
  }

  dp[0][0] = swim[0];
  dp[0][1] = bugs[0];
  dp[0][2] = homework[0];

  for(int i=1; i<N; i++) {
    // Taro swims in this turn
    dp[i][0] = max(dp[i-1][1]+swim[i], dp[i-1][2]+swim[i]);

    // Taro catches bug in this turn
    dp[i][1] = max(dp[i-1][0]+bugs[i], dp[i-1][2]+bugs[i]);

    // Taro does homework in this turn
    dp[i][2] = max(dp[i-1][0]+homework[i], dp[i-1][1]+homework[i]);
  }

  cout<<max(dp[N-1][0], max(dp[N-1][1], dp[N-1][2]))<<endl;
  return 0;
}
