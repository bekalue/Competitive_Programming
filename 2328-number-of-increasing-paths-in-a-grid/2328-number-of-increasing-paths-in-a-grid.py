class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        cells = [(grid[i][j], i, j) for i in range(m) for j in range(n)]
        cells.sort()
        for _, i, j in cells:
            dp[i][j] = 1
            for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] < grid[i][j]:
                    dp[i][j] += dp[ni][nj]
                    dp[i][j] %= MOD
        return sum(sum(row) for row in dp) % MOD
        