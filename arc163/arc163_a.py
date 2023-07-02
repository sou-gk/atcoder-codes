def can_split_string(S):
    n = len(S)
    for i in range(1, n):
        if S[i-1] >= S[i]:
            return True
    return False

# テストケース数を取得
T = int(input())

# 各テストケースに対して答えを求める
for _ in range(T):
    # 文字列Sを取得
    S = input()

    # 文字列Sを分割して連続部分文字列になるか判定
    if can_split_string(S):
        print("Yes")
    else:
        print("No")
