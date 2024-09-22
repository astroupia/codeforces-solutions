def solve():
    n = int(input())
    scores = {}
    for _ in range(n):
        team = input()
        if team in scores:
            scores[team] += 1
        else:
            scores[team] = 1
    print(max(scores, key=scores.get))

solve()
