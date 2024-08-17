from collections import Counter

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        freq = Counter(a)
        distinct_types = len(freq)
        
        counts = sorted(freq.values(), reverse=True)
        result = []
        
        for k in range(1, n + 1):
            if k <= distinct_types:
                result.append(distinct_types)
            else:
                result.append(distinct_types + (k - distinct_types))
        
        print(" ".join(map(str, result)))

solve()
