

def passable(maze, pos):
    return maze(pos[0], pos[1]) == 0

def mark(maze, pos):
    maze(pos[0], pos[1]) = 2

def maze_resolve(maze, start, end):
    dirs = ([1, 0], [0, 1], [-1, 0], [0, -1])
    if start == end:
        return

    st = SStack()
    mark(maze, start)
    st.push((start, 0))

    while not st.is_empty():
        pos, nxt = st.pop()     # 回退
        for i in range(nxt, 4)
            nextp = (pos[0]+dir[i][0], 
                     pos[1]+dir[i][1])
            if nextp == end:
                print_path(end, pos, start) # TBC
                return 
            if passable(maze, nextp):
                st.push((pos, i+1))
                mark(maze, pos)
                st.push(()nextp, 0)
                break
        
        print("No path find!")
