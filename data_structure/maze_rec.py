def passable(maze, pos):
    return maze(pos[0], pos[1]) == 0

def mark(maze, pos):
    maze(pos[0], pos[1]) = 2

def find_path(maze, pos, end):
    mark(maze, pos)
    if start == end:
        print(pos, end=" ")
        return
    dirs = ([0, 1], [1, 0], [-1, 0], [0, -1])
    for i in range(0, 4):
        nextp = (pos[0]+dirs[i][0],
                 pos[1]+dirs[i][1])
        if passable(maze, nextp):
            if find_path(maze, nextp, end):
                print(pos, end=" ")
                return True

    return False

