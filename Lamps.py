import heapq

def solve():
    data = input().split()
    index = 0
    t = int(data[index])
    index += 1
    results = []
    
    for _ in range(t):
        n = int(data[index])
        index += 1
        lamps = []
        for _ in range(n):
            a = int(data[index])
            b = int(data[index + 1])
            index += 2
            lamps.append((a, b))
        
        lamps.sort()
        
        max_heap = []
        total_points = 0
        turned_on = 0
        
        for a, b in lamps:
            if turned_on < a:
                heapq.heappush(max_heap, -b)
                total_points += b
                turned_on += 1
            else:
                if max_heap and -max_heap[0] < b:
                    total_points += b + heapq.heappop(max_heap)
                    heapq.heappush(max_heap, -b)
        
        results.append(total_points)
    
    print("\n".join(map(str, results)))
solve()