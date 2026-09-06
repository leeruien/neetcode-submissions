class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = []
        height = len(grid)
        width = len(grid[0])
        fresh = {}
        for i in range(height):
            for j in range(width):
                if grid[i][j] == 2:
                    rotten.append((i,j))
                elif grid[i][j]==1:
                    fresh[(i,j)] = 1
        # print(fresh, rotten)
        if fresh=={} and rotten!=[]: return 0
        if fresh!={} and rotten==[]: return -1
        if rotten==[] and fresh=={}: return 0 
        # n2 alr
        minutes = 0
        rotted = 0
        new_rotted = []
        while True:
            rotted = 0
            # print(rotten)
            for oranges in rotten:
                # print(oranges)
                i,j = oranges
                if (i - 1 >=0) and grid[i-1][j] == 1:
                    new_rotted.append((i-1,j))
                    rotted = 1
                    grid[i-1][j]=2
                    del fresh[(i-1,j)]
                if (i +2<=height) and grid[i+1][j] == 1:
                    new_rotted.append((i+1,j))
                    grid[i+1][j]=2
                    rotted = 1
                    del fresh[(i+1,j)]
                if (j-1>=0) and grid[i][j-1] == 1:
                    new_rotted.append((i,j-1))
                    grid[i][j-1]=2
                    rotted = 1
                    del fresh[(i,j-1)]
                if (j +2<=width) and grid[i][j+1] == 1:
                    new_rotted.append((i,j+1))
                    grid[i][j+1]=2
                    rotted = 1
                    print(i,j+1)
                    del fresh[(i,j+1)]
                # print("fresh:", fresh, "rotten: ", rotten, "rotted: ", rotted)
            # for that level 
            if (rotted == 1) and (fresh != {}): 
                minutes += 1
                rotten = new_rotted
                new_rotted = []
            elif (rotted==0) and (fresh != {}): 
                # print("here")
                return -1
            elif (rotted == 1) and (fresh == {}): 
                minutes += 1
                return minutes
            # print("minutes:", minutes)
        return -1

