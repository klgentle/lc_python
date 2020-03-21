def ack(m, n):
    if m == 0:
        return n+1
    if n == 0:
        return ack(m-1, 1)

    return ack(m-1, ack(m, n-1))


print(ack(3, 4))
"""
ack(0,0) = -1
ack(0,1) = -1
ack(1,0) = ack(0,1) = -1
ack(1,1) = ack(0,ack(1,0)) = ack(0,-1) = -1
ack(1,2) = ack(0,ack(1,1)) = -1
ack(2,0) = ack(1,0) = -1
ack(2,1) = ack(1,ack(2,0)) = ack(1,-1) = ack(0,..) = -1
ack(2,2) = ack(1,ack(2,1))
 """
