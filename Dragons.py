def can_defeat_dragons(kirito_strength, dragons):
    dragons.sort(key=lambda x: x[0])
    
    for dragon_strength, bonus in dragons:
        if kirito_strength <= dragon_strength:
            return "NO"
        kirito_strength += bonus
    
    return "YES"

s, n = map(int, input().split())
dragons = [tuple(map(int, input().split())) for _ in range(n)]

result = can_defeat_dragons(s, dragons)
print(result)
