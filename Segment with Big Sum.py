def segment_with_big_sum(n, s, a):
    left = 0
    current_sum = 0
    min_length = float('inf')

    for right in range(n):
        current_sum += a[right]

        while current_sum >= s:
            min_length = min(min_length, right - left + 1)
            current_sum -= a[left]
            left += 1

    print(min_length if min_length != float('inf') else -1)

n, s = map(int, input().split())
a = list(map(int, input().split()))
segment_with_big_sum(n, s, a)
