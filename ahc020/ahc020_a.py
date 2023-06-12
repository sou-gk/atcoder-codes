# 各スイッチの使用回数を計算
switch_count = [0] * m
for i in range(n):
    for j in range(m):
        if a[i][j] == 1:
            switch_count[j] += 1

# 使用回数が多い順にスイッチを並べ替え
sorted_switches = sorted(range(m), key=lambda x: switch_count[x], reverse=True)

# スイッチのON/OFFを決定
switch_status = [0] * m
for i in sorted_switches:
    # スイッチをONにした場合の他のスイッチの使用回数増分を計算
    diff = sum(a[j][i] * (1 - switch_status[j]) for j in range(n))
    # 増分が最も大きいスイッチをONにする
    if diff > 0:
        switch_status[i] = 1

# スイッチのONの個数を出力
print(sum(switch_status))
