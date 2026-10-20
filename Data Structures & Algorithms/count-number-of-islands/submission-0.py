class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        # find first one by going from top left to bottom right
        # then do breadth-first-search  to classify points at connecting to that island

        islands = 0
        explored = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]

        def bfs(i, j):

            q = deque([(i, j)])
            island = [(i, j)]

            while q:

                node = q.popleft()
                i, j = node
                neighbours = [(i-1, j), (i, j-1), (i+1, j), (i, j+1)]

                for neighbour in neighbours:

                    m, n = neighbour

                    if m < 0 or n < 0 or m > len(grid) - 1 or n > len(grid[0]) - 1:
                        continue 

                    if explored[m][n] == 0:
                        explored[m][n] = 1
                    else:
                        continue
                    
                    if grid[m][n] == "0":
                        continue

                    island.append(neighbour)
                    q.append(neighbour)    
                        

            return island
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):

                if explored[i][j] == 0:
                    explored[i][j] = 1
                else:
                    continue
                
                if grid[i][j] == "0":
                    continue
                
                bfs(i, j)
                islands += 1
        return islands

