s = input().strip()
n = len(s)

prefix_sum = [0] * (n + 1)
for i in range(1, n):
    prefix_sum[i] = prefix_sum[i-1] + (s[i] == s[i-1])

m = int(input())
for _ in range(m):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    result = prefix_sum[r] - prefix_sum[l]
    print(result)
