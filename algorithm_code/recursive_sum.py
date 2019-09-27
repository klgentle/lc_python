def recusive_sum(arr):
    if len(arr) == 1:
        return arr[-1]
    else:
        return arr.pop() + recusive_sum(arr)


if __name__ == "__main__":
    # li = [1, 2, 3, 4]
    li = [2, 4, 6]
    print(recusive_sum(li))
