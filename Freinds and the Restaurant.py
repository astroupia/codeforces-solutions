def max_restaurant_days(n, x, y):
    differences = sorted([y[i] - x[i] for i in range(n)])
    left, right = 0, n - 1
    days = 0

    while left < right:
        if differences[left] + differences[right] >= 0:
            days += 1
            left += 1
            right -= 1
        else:
            left += 1

    return days

t = int(input())
for _ in range(t):
    n = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    print(max_restaurant_days(n, x, y))
