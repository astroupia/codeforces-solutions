def solve():
    data = input().strip()
    index = 0
    t = int(data[index])
    index += 1
    results = []
    
    for _ in range(t):
        n = int(data[index])
        index += 1
        a = list(map(int, data[index:index + n]))
        index += n
        
        # Look for a subsegment [i, i+1] where neither end is min or max
        found = False
        for i in range(n - 1):
            if a[i] < a[i + 1]:
                # Check if the subsegment [i, i+1] is valid
                min_val = a[i]
                max_val = a[i + 1]
            else:
                min_val = a[i + 1]
                max_val = a[i]
            
            if (a[i] != min_val and a[i] != max_val and
                a[i + 1] != min_val and a[i + 1] != max_val):
                results.append(f"{i + 1} {i + 2}")
                found = True
                break
        
        if not found:
            results.append("-1")
    
    sys.stdout.write("\n".join(results) + "\n")

solve()