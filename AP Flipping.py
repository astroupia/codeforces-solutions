import sys

def solve():
    n = int(input())
    s = input().strip()
    
    ans = n - 1
    
    # Remove leading 'B' characters
    for i in range(n):
        if s[i] == 'B':
            ans -= 1
        else:
            break
    
    # Remove trailing 'A' characters
    for j in range(n-1, -1, -1):
        if s[j] == 'A':
            ans -= 1
        else:
            break
    
    ans = max(ans, 0)
    print(ans)

def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
