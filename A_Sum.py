num =  int(input())

for _ in range(num):
    nums = list(map(int, input().split()))
    nums.sort()
    if (nums[0] + nums[1]) == nums[2]:
        print("YES")
    else:
        print("NO")