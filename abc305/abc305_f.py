# 必要なライブラリをインポート
from sys import stdout

# 隣接する頂点を問い合わせる関数
def query(v):
    print(v)
    stdout.flush()
    return int(input())

# 頂点1から頂点Nへ移動する関数
def move():
    # 頂点1からスタート
    cur = 1
    # 隣接する頂点を調べながら、頂点Nへ移動する
    while True:
        # 頂点Nに到達したら終了
        if cur == N:
            break
        # 隣接する頂点を調べる
        nxt = query(cur)
        # 隣接する頂点が頂点Nなら、頂点Nへ移動して終了
        if nxt == N:
            print(nxt)
            stdout.flush()
            return
        # 隣接する頂点が頂点N以外なら、その頂点に移動する
        cur = nxt

# グラフの情報を受け取る
N, _ = map(int, input().split())

# 頂点1から頂点Nへ移動する
move()
