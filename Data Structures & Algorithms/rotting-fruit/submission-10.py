class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        fresh_counts = 0
        rotten_stack = []
        minute = 0
        new_minute_stack = []
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    fresh_counts += 1
                elif grid[i][j] == 2:
                    rotten_stack.append((i, j))

        while rotten_stack:

            i, j = rotten_stack.pop()

            if i != len(grid) - 1 and grid[i+1][j] == 1:
                new_minute_stack.append((i+1, j))
                grid[i+1][j] = 2
                fresh_counts -= 1

            if grid[i-1][j] == 1 and i != 0:
                new_minute_stack.append((i-1, j))
                grid[i-1][j] = 2
                fresh_counts -= 1
            
            if j != len(grid[i]) - 1 and grid[i][j + 1] == 1:
                grid[i][j+1] = 2
                new_minute_stack.append((i, j+1))
                fresh_counts -= 1

            if grid[i][j-1] == 1 and j != 0:
                grid[i][j-1] = 2
                new_minute_stack.append((i, j - 1))
                fresh_counts -= 1
            
            if not rotten_stack and new_minute_stack:
                minute += 1
                rotten_stack = new_minute_stack
                new_minute_stack = []
        
        if fresh_counts:
            return -1

        return minute
        