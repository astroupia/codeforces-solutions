import sys
length, s = map(int, input().split())
nums = list(map(int, input().split()))

def goodSum(s, nums, len):
    a, res, x = 0, sys.maxsize, 0
    for i in range(0, len) :
        x += nums[i]
        while x >= s:
            res = min(res, i - a +1)
            x -= nums[a]
            a += 1

    if res != sys.maxsize:
        return(res)
    else:
        return -1

print(goodSum(s, nums, length))