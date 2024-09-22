n = int(input())
times = list(map(int, input().split()))

alice = 0
bob = 0
alice_time = 0
bob_time = 0
left = 0
right = n - 1

while left <= right:
    if alice_time <= bob_time:
        alice_time += times[left]
        alice += 1
        left += 1
    else:
        bob_time += times[right]
        bob += 1
        right -= 1

print(alice, bob)
