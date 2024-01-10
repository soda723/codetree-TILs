from collections import deque

n = int(input())
grid = [
    list(map(int, input().split())) for _ in range(n)
]

def check_index(x,y):
    if 0<= x < n and 0<= y <n : return True
    else : return False

nums = []
for x in range(n):
    for y in range(n):
        nums.append([grid[x][y], x, y])
nums.sort()
nums = deque(nums)
#print(nums)

dp = [[1]*n for _ in range(n)]
for v, x, y in nums:
    for dx, dy in [(-1,0),(1, 0), (0, -1), (0,1)]:
        nx = dx+x
        ny = dy+y
        if check_index(nx,ny) and grid[nx][ny] > v:
            dp[nx][ny] = max(dp[nx][ny],dp[x][y]+1)

print(max(map(max, dp)))