def is_lucky(num):
    while num > 0:
        digit = num % 10
        if digit != 4 and digit != 7:
            return False
        num //= 10
    return True

def generate_lucky_numbers(limit):
    from collections import deque
    
    lucky_numbers = set()
    queue = deque([4, 7])
    
    while queue:
        number = queue.popleft()
        if number > limit:
            continue
        lucky_numbers.add(number)
        queue.append(number * 10 + 4)
        queue.append(number * 10 + 7)
    
    return lucky_numbers

def solve():
    n = int(input())
    
    lucky_numbers = generate_lucky_numbers(1000)
    
    for lucky in lucky_numbers:
        if n % lucky == 0:
            print("YES")
            return
    
    print("NO")

solve()