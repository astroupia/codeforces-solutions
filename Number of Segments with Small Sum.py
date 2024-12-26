length, s = map(int, input().split())
nums = list(map(int, input().split()))

def goodSum(s, nums, len):
    a, res, x = 0, 0, 0
    for i in range(len) :
        x += nums[i]
        while x >= s:
            x -= nums[a]
            a += 1
        res += a
    return res

print(goodSum(s, nums, length))