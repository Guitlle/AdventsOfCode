import itertools
with open("day9.input") as f:
    inputd = f.readlines()

testdata = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576""".split("\n")

#data = [int(x) for x in testdata]
data = [int(x) for x in inputd]
prevn = 25
size = len(data)
ix = 0
for i in range(prevn, size-1):
    combinaciones = list(itertools.combinations(data[i-prevn:i], 2))
    posibles = [x+y for x,y in combinaciones]
    if data[i] not in posibles:
        print(i, data[i])
        ix = i
        break

resp1 = data[ix]

suma = 0
inicio = 0
for j in range(0, ix):
    suma += data[j]
    while suma > resp1:
        suma -= data[inicio]
        inicio+=1
    if suma == resp1:
        print(min(data[inicio:j]) + max(data[inicio:j]))
        break
        