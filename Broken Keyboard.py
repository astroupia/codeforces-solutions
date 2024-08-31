t = int(input())  # Number of test cases

for _ in range(t):
    s = input().strip()  # The string from the screen
    working_buttons = set()
    i = 0
    n = len(s)

    while i < n:
        count = 1
        while i + 1 < n and s[i] == s[i + 1]:
            count += 1
            i += 1
        if count % 2 == 1:
            working_buttons.add(s[i])
        i += 1

    # Output the characters in alphabetical order
    print(''.join(sorted(working_buttons)))
