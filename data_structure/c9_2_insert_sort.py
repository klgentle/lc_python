def insert_sort(lst):
    for i in range(1, len(lst)):  # 开始时片段[0:1]已排序
        x = lst[i]
        j = i
        while j > 0 and lst[j - 1].key > x.key:
            lst[j] = lst[j - 1]  # 反序逐个后移元素，确定插入位置
            j -= 1
        lst[j] = x
