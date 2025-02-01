num = int(input())
target = "codeforces"

for _ in range(num):
    strs = input().strip()
    count = 0
    for i in range(len(target)):      
        if strs[i] != target[i]:
            count += 1
    print(count)
