def main():
    for c in range(1,100):
        if is_prime(c):
            print(c)

def is_prime(v):
    if v<2:
        return False
    elif v==2:
        return True
    else:
        i=2
        while i<v:
            if((v%i)==0):
                return False
            else:
                i+=1
        return True

main()
