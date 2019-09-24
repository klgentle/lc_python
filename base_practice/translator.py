def jiugongge_letter_to_number(phoneNum) -> str:
    """老手机中的九宫格字母转为对应的数字"""
    # phoneNum = input("Enter a phone number to be translated: ")
    # phoneNum = "555-GET-FOOD"
    phoneNum = phoneNum.upper()
    phoneNum_list = phoneNum.split("-")

    # ['555','GET','FOOD']
    for j in range(len(phoneNum_list)):
        # 'GET'
        var = phoneNum_list[j]
        if var.isdigit():
            continue
        var2 = [0] * len(var)
        for i in range(len(var)):
            if var[i] == "A" or var[i] == "B" or var[i] == "C":
                var2[i] = "2"
            elif var[i] == "D" or var[i] == "E" or var[i] == "F":
                var2[i] = "3"
            elif var[i] == "G" or var[i] == "H" or var[i] == "I":
                var2[i] = "4"
            elif var[i] == "J" or var[i] == "K" or var[i] == "L":
                var2[i] = "5"
            elif var[i] == "M" or var[i] == "N" or var[i] == "O":
                var2[i] = "6"
            elif var[i] == "P" or var[i] == "Q" or var[i] == "R" or var[i] == "S":
                var2[i] = "7"
            elif var[i] == "T" or var[i] == "U" or var[i] == "V":
                var2[i] = "8"
            elif var[i] == "W" or var[i] == "X" or var[i] == "Y" or var[i] == "Z":
                var2[i] = "9"
        # print(f"var2:{var2}")
        phoneNum_list[j] = "".join(var2)

    phoneNum1 = "-".join(phoneNum_list)
    # print(phoneNum1)
    return phoneNum1


if __name__ == "__main__":
    phoneNum = input("Enter a phone number to be translated: ")
    print(jiugongge_letter_to_number(phoneNum))
