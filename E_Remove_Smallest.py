num = int(input())

for _ in range(num):
    i = int(input())
    x = list(map(int, input().split()))
    x.sort()
    possible = True 
    for n in range(i):
        if x[n] - x[n-1] > 1:
            possible = False
            break
    print("YES" if possible == True else "NO")