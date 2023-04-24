#すべての長さをx以上にできるかどうか判定する関数
def is_cutable(x, N, A):
  #何回切ったか
  num = 0
  #最後に切ったのはいつか
  pre = 0
  
  #xを超えたタイミングで切っていく
  for i in range(N):
    if A[i] - pre >= x:
      num += 1
      pre = A[i]
      
  #Lから最後のpreまでのあまりも、x以上なら切ったと考える
  if L - pre >= x:
    num += 1
  
  #numにはx以上の切れ端の数が格納されている。
  #numがK+1を超える→切れ端をK+1個用意できる→K回切った上で最小の切れ端はx以上
  return (num >= K + 1)
 
[N, L] = list(map(int, input().split()))
K = int(input())
A = list(map(int, input().split()))

#二分探索(最大のxを探しにゆくのさ)
left = -1
right = L+1

while (right - left) > 1:
  mid = (left + right) // 2
  
  #midになるよう切れるなら探索範囲はmidより上側
  if is_cutable(mid, N ,A):
    left = mid
  
  #midになるよう切れないなら探索範囲はmidより下側
  else:
    right = mid

print(left)
