from collections import Counter
t = int(input())

def helper(s,t,p):
    
    found = Counter(p)

    if len(s) > len(t):
        return "NO"
    
    st, right = 0, 0
    while right < len(t):
        
        if st<len(s) and s[st] == t[right]:
            st += 1
            right += 1

        elif t[right] in found and found[t[right]] > 0:
            found[t[right]] -= 1
            right += 1

        else:
            return "NO"
    
    if st < len(s):
        return "NO"

    return "YES"
                


for _ in range(t):
    s = list(input())
    t = list(input())
    p = list(input())

    print(helper(s,t,p))