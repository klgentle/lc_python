"""
背包问题
一个背包，可以装下weight的重量. 现在一个集合S, 里面有多个物品，请写一个程序，判断是否存在若干件个物品，刚好重量为weight
-----提示：
考虑最后一件物品
"""


def knap_rec(weight, wlist, n):
    if weight == 0:
        return True
    if weight < 0 or (weight > 0 and n < 1):
        return False

    # 考虑第n件物品
    if knap_rec(weight - wlist[n - 1], wlist, n - 1):
        print(f"Item {n}: {wlist[n-1]}")
        return True
    # 不考虑第n件物品
    if knap_rec(weight, wlist, n - 1):
        return True
    else:  # 思考这个else 可以不可以去掉? 好像可以
        return False
