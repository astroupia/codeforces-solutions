def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    tc = int(data[0])
    index = 1

    for _ in range(tc):
        str = data[index]
        index += 1

        one = 0
        n = len(str)
        str += str

        i = 0
        while i < len(str):
            j = i
            while j < len(str) and str[j] == '1':
                j += 1
            one = max(one, j - i)
            i = j

        if one == 0:
            print(0)
        else:
            if one > n:
                print(n * n)
            else:
                if one % 2 == 1:
                    print(((one + 1) // 2) ** 2)
                else:
                    print(((one + 2) // 2) * (one // 2))

if __name__ == "__main__":
    main()
