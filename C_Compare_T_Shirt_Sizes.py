num = int(input())

for _ in range(num):
    a, b = map(str, input().split())

    if a == b:
        print("=")
    elif a[-1] == b[-1]:
        if a[-1] == "L":
            print("<" if len(a) < len(b) else ">")
        elif a[-1] == "S":
            print(">" if len(a) < len(b) else "<")
        else:
            print("=")
    else:
        if a[-1] == "S":
            print("<")
        elif a[-1] == "L":
            print(">")
        else:
            if b[-1] == "S":
                print("<")
            else:
                print(">")
