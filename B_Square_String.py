num = int(input().strip())  

for _ in range(num):
    s = input().strip()
    if len(s) % 2 != 0:
        print("NO")
    else:
        mid = len(s) // 2
        if s[:mid] == s[mid:]:
            print("YES")
        else:
            print("NO")
