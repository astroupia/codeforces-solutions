aSize, bSize = map(int, input().split())
firstArray = list(map(int, input().split()))
secondArray = list(map(int, input().split()))
 
def findEqual(a, b):
    k, l, count = 0, 0, 0
    
    while k < len(a) and l < len(b):
        if a[k] < b[l]:
            k += 1
        elif a[k] > b[l]:
            l += 1
        else: 
            ck = a[k]
            cl = b[l]
            countA, countB = 0, 0
            
            while k < len(a) and a[k] == ck:
                k += 1
                countA += 1
            
            while l < len(b)  and b[l] == cl:
                l += 1
                countB += 1
                
            count += countA * countB
    return count
 
result = findEqual(firstArray, secondArray)
print(result)