with open("day6.input") as f:
    inputd = f.readlines()

nlines = len(inputd)
total = 0
registro = ""
for i, line in enumerate(inputd):
    registro += line
    if line == "\n" or i+1 == nlines:
        distintos = set(list(registro))
        distintos.discard("\n")
        total += len(distintos)
        registro = ""
print(total)

from functools import reduce

total = 0
registro = []
for i, line in enumerate(inputd):
    registro.append(line[:-1])
    if line == "\n" or i+1 == nlines:
        registro.pop()
        intersections = reduce(lambda x, y: x.intersection(y), 
                        [ set(x) for x in registro])
        total += len(intersections)
        registro = []
print(total)