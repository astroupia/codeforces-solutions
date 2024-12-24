length = int(input())
nums = list(map(int, input().split()))

def findBarsConsumed (nums):
    a, i, aliceTime, bobTime = (length - 1), 0, 0, 0
    alice, bob = 0, 0
    while i <= a:
        if aliceTime <= bobTime:
            aliceTime += nums[i]
            alice += 1
            i += 1
        else:
            bobTime += nums[a]
            bob += 1
            a -= 1
        
    res = [alice, bob]
    return res

print(" ".join(map(str, findBarsConsumed(nums))))
