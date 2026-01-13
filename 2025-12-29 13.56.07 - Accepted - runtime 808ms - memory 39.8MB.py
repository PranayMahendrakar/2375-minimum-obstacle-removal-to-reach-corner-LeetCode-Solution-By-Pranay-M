class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        # 0-1 BFS: empty cell cost 0, obstacle cost 1
        # Time: O(m*n), Space: O(m*n)
        from collections import deque
        
        m, n = len(grid), len(grid[0])
        dist = [[float('inf')] * n for _ in range(m)]
        dist[0][0] = 0
        
        # Deque for 0-1 BFS
        dq = deque([(0, 0, 0)])  # (obstacles, row, col)
        
        while dq:
            obstacles, r, c = dq.popleft()
            
            if r == m - 1 and c == n - 1:
                return obstacles
            
            if obstacles > dist[r][c]:
                continue
            
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    new_cost = obstacles + grid[nr][nc]
                    if new_cost < dist[nr][nc]:
                        dist[nr][nc] = new_cost
                        if grid[nr][nc] == 0:
                            dq.appendleft((new_cost, nr, nc))
                        else:
                            dq.append((new_cost, nr, nc))
        
        return dist[m-1][n-1]