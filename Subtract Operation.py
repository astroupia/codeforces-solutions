t = int(input())  # Number of test cases

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    found = False
    seen = set()

    for x in a:
        if (x - k) in seen or (x + k) in seen:
            found = True
            break
        seen.add(x)

    if found:
        print("YES")
    else:
        print("NO")
