def is_valley(arr):
    n = len(arr)
    left = 0
    right = n - 1
    
    # Find the left boundary of the potential valley
    while left < n - 1 and arr[left] >= arr[left + 1]:
        left += 1
    
    # Find the right boundary of the potential valley
    while right > 0 and arr[right] >= arr[right - 1]:
        right -= 1
    
    # Check if there's only one flat bottom between left and right
    return left >= right or all(arr[i] == arr[left] for i in range(left, right + 1))

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print("YES" if is_valley(arr) else "NO")
