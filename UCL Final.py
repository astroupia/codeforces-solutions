def solve():
    x = int(input())
    scores = {}
    for _ in range(x):
        team = input()
        if team in scores:
            scores[team] += 1
        else:
            scores[team] = 1
    print(max(scores, key=scores.get))

solve()
