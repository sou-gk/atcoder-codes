H, W = map(int, input().split())
grid = [input() for _ in range(H)]

for i in range(1, H):
    for j in range(1, W):
        if grid[i][j] == ".":
            continue
        if grid[i-1][j] == "#" and grid[i][j-1] == "#" and grid[i-1][j-1] == "#":
            print(i, j)
            exit()
        if grid[i-1][j] == "." and grid[i][j-1] == "." and grid[i-1][j-1] == ".":
            print(i, j)
            exit()
