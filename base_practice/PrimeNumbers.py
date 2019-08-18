n=int(input("Enter an integer:"))
def is_prime(n):
    if n<2:
        return False
    elif n==2:
        return True
    else:
        i=2
        while i<n:
             if((n%i)==0):
                  return False
             else:
                 i+=1
        return True
print(is_prime(n))
