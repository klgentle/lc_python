import sys
import heapq

def solve():
    fl_jd_data = sys.stdin.read().split()
    if not fl_jd_data:
        return
    
    n = int(fl_jd_data[0])
    reqs = list(map(int, fl_jd_data[1:n + 1]))
    durs = list(map(int, fl_jd_data[n + 1:]))
    
    tasks = sorted(zip(reqs, durs))
    
    curr_time = 0
    total_wait = 0
    idx = 0
    q = []
    
    while idx < n or q:
        if not q and curr_time < tasks[idx][0]:
            curr_time = tasks[idx][0]
        
        while idx < n and tasks[idx][0] <= curr_time:
            heapq.heappush(q, (tasks[idx][1], tasks[idx][0]))
            idx += 1
            
        dur, req = heapq.heappop(q)
        total_wait += (curr_time - req)
        curr_time += dur
        
    print(f"{total_wait / n:.2f}")

if __name__ == '__main__':
    solve()