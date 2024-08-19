def solve():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        s = input()

        lower = [0] * 26
        upper = [0] * 26

        for char in s:
            if char.islower():
                lower[ord(char) - ord('a')] += 1
            else:
                upper[ord(char) - ord('A')] += 1

        pairs = 0
        surplus = 0

        for i in range(26):
            match = min(lower[i], upper[i])
            pairs += match
            surplus += (lower[i] - match) // 2 + (upper[i] - match) // 2

        print(pairs + min(surplus, k))

solve()
