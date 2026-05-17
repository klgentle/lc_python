import sys

def solve():
	data = list(map(int, sys.stdin.read().split()))
	if not data:
		return
	n = data[0]
	nums = data[1:n+1]
	k = data[n+1]
	
	result = sorted(nums[:k]) + sorted(nums[k:], reverse=True)
	print(*(result))
	
if __name__ == "__main__":
	solve()