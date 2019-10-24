def josephus_a(total_num, start, target_num):
    """
    假设有n个人围坐一圈，现要求从第 k 个人开始报数,报到第 m 个数的人退出
    """
    people = list(range(1, total_num + 1))

    index = start - 1
    for times in range(total_num):
        count = 0
        while count < target_num:
            if people[index] > 0:
                count += 1
            if count == target_num:
                print(people[index], end="")
                people[index] = 0
            index = (index + 1) % total_num
        if times < total_num - 1:
            print(", ", end="")
        else:
            print("")

    return


if __name__ == "__main__":
    josephus_a(5, 2, 2)
