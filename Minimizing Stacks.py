from collections import Counter

def solve():
    n = int(input())  
    lengths = list(map(int, input().split())) 
    
    frequency = Counter(lengths)
    tallest_tower = max(frequency.values())
    number_of_towers = len(frequency)
    print(tallest_tower, number_of_towers)

solve()
