import re

strs = input()

def sort_equation(strs):
    exp = re.sub(r'[^0-9]', '', strs)
    lst = list(exp)
    lst.sort()
    return "+".join(lst)

print(sort_equation(strs))