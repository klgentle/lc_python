try:
    file = open("text.txt", "rb")
except IOError as e:
    print("An IOError occured. {}".format(e.args[-1]))
