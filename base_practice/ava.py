number_file = open("numbers.txt", "r")
total = 0
count = 0
ave = 0
num = number_file.readline()
while num != "":
    amount = int(num)
    total += amount
    count += 1
    num = number_file.readline()

number_file.close()
ave = total / count
print(format(ave, ".1f"))
