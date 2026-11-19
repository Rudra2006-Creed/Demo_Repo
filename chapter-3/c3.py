n = int(input())
numbers = list(map(int,input().split()))

dct = {}

for i in numbers:
    if i not in dct:
        dct[i] = 1

    else: 
        dct[i] += 1

for key, value in dct.items():
    if value == 1:
        print(key, end = " ")
