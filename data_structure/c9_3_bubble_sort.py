def bubble_sort(lst):
    for i in range(len(lst)):
        #一次完整的扫描（比较和交换）能保证把一个最大的元素移到到未排序部分的最后
        for j in range(1, len(lst) - i):
            if lst[j - 1].key > lst[j].key:
                lst[j - 1], lst[j] = lst[j], lst[j - 1]


def bubble_sort2(lst):
    """改进：如果在一次扫描中没有遇到逆序，说明排序工作已经完成，可以提前结束了"""
    for i in range(len(lst)):
        found = False
        #一次完整的扫描（比较和交换）能保证把一个最大的元素移到到未排序部分的最后
        for j in range(1, len(lst) - i):
            if lst[j - 1].key > lst[j].key:
                lst[j - 1], lst[j] = lst[j], lst[j - 1]
                found = True
        if not found:
            break
