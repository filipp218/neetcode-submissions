class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        stack = []
        count_of_island = 0
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1" and (i, j) not in visited:
                    count_of_island += 1
                    stack.append((i, j))
                    while stack:
                        i_i, i_j = stack.pop()
                        if (i_i, i_j) in visited:
                            continue

                        visited.add((i_i, i_j))
                        if i_i != 0:
                            if grid[i_i - 1][i_j] == "1":
                                stack.append((i_i - 1, i_j))
                        if i_i != len(grid) - 1:
                            if grid[i_i + 1][i_j] == "1":
                                stack.append((i_i + 1, i_j))
                        if i_j != 0:
                            if grid[i_i][i_j - 1] == "1":
                                stack.append((i_i, i_j - 1))
                        
                        if i_j != len(grid[i_i]) - 1:
                            if grid[i_i][i_j + 1] == "1":
                                stack.append((i_i, i_j+1))
        return count_of_island
        