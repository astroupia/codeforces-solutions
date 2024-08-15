aSize, bSize = map(int, input().split())
firstArray = list(map(int, input().split()))
secondArray = list(map(int, input().split()))

def mergeArray(a, b):
    aIndicator, bIndicator = 0, 0
    newArray = []
    
    while aIndicator < len(a) and bIndicator < len(b):
        if a[aIndicator] < b[bIndicator]:
            newArray.append(a[aIndicator])
            aIndicator += 1
            
        else:
            newArray.append(b[bIndicator])
            bIndicator += 1

    while aIndicator < len(a):
        newArray.append(a[aIndicator])
        aIndicator += 1

    while bIndicator < len(b):
        newArray.append(b[bIndicator])
        bIndicator += 1

    return newArray

print(" ".join(map(str,mergeArray(firstArray, secondArray))))