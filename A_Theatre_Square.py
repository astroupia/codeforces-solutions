from math import ceil 
n, m, a = map(int, input().split())

def sqaure_theatre(n, m, a):
    print(((n + a - 1 )// a) * ((m + a - 1)//a))

sqaure_theatre(n, m, a)