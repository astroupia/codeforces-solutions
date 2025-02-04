num = int(input())
strs = input()


counter = 0
lst = []
i = 0
while i < len(strs):
    counter += 1
    lst.append(strs[i])
    i += counter

print("".join(lst))