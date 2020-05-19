def select_sort(lst):
    for i in range(len(lst) - 1):  # 只需循环 len(lst) -1 次
        k = i
        for j in range(i, len(lst)):  # k 是已知最小元素的位置
            if lst[j].key < lst[k].key:
                k = j
        if i != k:  # lst[k] 是确定的最小元素，检查是否需要交换
            lst[i], lst[k] = lst[k], lst[i]
