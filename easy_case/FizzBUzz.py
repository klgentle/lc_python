def FizzBuzz(n):
    for i in range(1,n+1):
        #print('test,i:{}'.format(i))
        if i % 3 == 0:
            if i % 5 == 0:
                print("FizzBuzz")
            else:
                print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print("{}".format(i))

if __name__ == '__main__':
    FizzBuzz(100)
