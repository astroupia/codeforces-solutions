aSize, bSize = map(int, input("").split())
firstArray = list(map(int, input().split()))
secondArray = list(map(int, input().split()))

def findSmallArray(a, b):
    aIndicator = 0
    newArray = []
    
    for i in range(len(b) - 1):
        while aIndicator < len(a) and a[aIndicator] < b[i]:
            aIndicator += 1  
        newArray.append(aIndicator)

    return newArray

print(" ".join(map(str,findSmallArray(firstArray, secondArray))))