import sys

def main():
    d = sys.stdin.read().split()
    if not d:
        return
    n = int(d[0])
    pts = {(int(d[i * 2 + 1]), int(d[i * 2 + 2])) for i in range(n)}
    c = 0
    while pts:
        if len(pts) <= 2:
            c += 1
            break
        b, p1 = set(), next(iter(pts))
        for p2 in pts:
            if p1 == p2:
                continue
            dx, dy = p2[0] - p1[0], p2[1] - p1[1]
            cur = {p for p in pts if (p[1] - p1[1]) * dx == dy * (p[0] - p1[0])}
            if len(cur) > len(b):
                b = cur
        pts -= b if b else {p1}
        c += 1
    print(c)

if __name__ == '__main__':
    main()