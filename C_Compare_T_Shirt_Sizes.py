num = int(input())

for _ in range(num):
    a, b = map(str, input().split())

    if a[-1] == "S":
        if b[-1] == "S":
            if len(a) > len(b):
                print("<")
            elif len(a) < len(b):
                print(">")
            else:
                print("=")
        elif b[-1] == "L":
            print("<")
        else:
            print("<")
    elif a[-1] == "L":
        if b[-1] == "L":
            if len(a) > len(b):
                print(">")
            elif len(a) < len(b):
                print("<")
            else:
                print("=")
        elif b[-1] == "S":
            print(">")
        else:
            print(">")
    elif a[-1] == "M":
        if b[-1] == "S":
            print(">")
        elif b[-1] == "L":
            print("<")
        else:
            print("=")
                
        