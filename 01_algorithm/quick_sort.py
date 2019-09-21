def quick_sort(array):
    """快速排序"""
    if len(array) < 2:
        return array  # <---- base case
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]  # 所有小于等于基准值的元素
        greater = [i for i in array[1:] if i > pivot]  # 所有大于基准值的元素
        return quick_sort(less) + [pivot] + quick_sort(greater)


print(quick_sort([10, 2, 3, 5]))
