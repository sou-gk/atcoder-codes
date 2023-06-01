x, k, d = map(int, input().split())

x = abs(x)  # 座標を非負の整数に変換

max_move = min(k, x // d)  # 最大で移動できる回数
remain = k - max_move  # 残りの移動回数

if remain % 2 == 0:
    ans = x - max_move * d  # 偶数回移動する場合
else:
    ans = x - (max_move + 1) * d  # 奇数回移動する場合

if ans < 0:
    ans = -ans

print(ans)
