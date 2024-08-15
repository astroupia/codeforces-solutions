aSize, bSize = map(int, input().split())
firstArray = list(map(int, input().split()))
secondArray = list(map(int, input().split()))

def findSmallArray(a, b):
    j, i = 0, 0
    count = 0

    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            i += 1
        elif a[i] > b[j]:
            j += 1
        else: 
            countA, countB = 0, 0
            currentA = a[i]
            currentB = b[j]

            while i < len(a) and a[i] == currentA:
                countA += 1
                i += 1
            
            while j < len(b) and b[j] == currentB:
                countB += 1
                j += 1

            count += countA * countB

    return count

print(findSmallArray(firstArray, secondArray))