import sys
input = sys.stdin.read

def solve(n, k, s):
    result = []
    
    for char in s:
        while k > 0 and result and result[-1] > char:
            result.pop()
            k -= 1
        
        result.append(char)

    while k > 0:
        result.pop()
        k -= 1
    
    print("".join(result))

# Read the input
data = input().strip().split()
n = int(data[0])
k = int(data[1])
s = data[2]

# Call the solve function
solve(n, k, s)
