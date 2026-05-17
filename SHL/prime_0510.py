import sys

def solve():
    try:
        input_data = sys.stdin.read().split()
        if not input_data:
            return
        num = int(input_data[0])
        if num < 2:
            return
        
        is_prime = [True] * (num + 1)
        for p in range(2, int(num**0.5) + 1):
            if is_prime[p]:
                for i in range(p * p, num + 1, p):
                    is_prime[i] = False
        
        print(*(i for i in range(2, num + 1) if is_prime[i]))
    except EOFError:
        pass

if __name__ == "__main__":
    solve()
