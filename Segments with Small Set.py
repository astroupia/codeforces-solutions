length, k = map(int, input().split())
nums = list(map(int, input().split()))

def findSmallSet (nums, k, leng):
    a, res = 0, 0
    freq = {}
    for i in range(leng):
        freq[nums[i]] = freq.get(nums[i], 0) + 1
        while len(freq) > k:
            freq[nums[a]] -= 1
            if freq[nums[a]] == 0:
                del freq[nums[a]]
            a += 1
        res += i - a + 1
    return res 

print(findSmallSet(nums, k, length))