import numpy as np

with open("day16.input") as f:
    inputd = f.readlines()

testdata = """class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12"""
#inputd = list(map(str.strip,testdata.split("\n")))
inputd = list(map(str.strip, inputd))

ix = 0
rules = {}
while inputd[ix] != "":
    temp = inputd[ix].split(": ")
    rangos = temp[1].split(" or ")
    rules[temp[0]] = {
        "r1": list(map(int, rangos[0].split("-"))),
        "r2": list(map(int, rangos[1].split("-")))
    }
    ix += 1

while inputd[ix] != "your ticket:":
    ix += 1
myticket = [int(x) for x in inputd[ix+1].split(",")]
while inputd[ix] != "nearby tickets:":
    ix += 1

errores_p1 = []
goodrows = []
gooddata = []
for linea in inputd[ix+1:]:
    ns = [int(x) for x in linea.split(",")]
    badrow = False
    for n in ns:
        rtests = []
        for regla in rules.values():
            rtests.append((regla["r1"][0] <= n and regla["r1"][1] >= n) or \
               (regla["r2"][0] <= n and regla["r2"][1] >= n) )
        if not any(rtests):
            errores_p1.append(n)
            badrow = True
    if not badrow:
        goodrows.append(linea)
        gooddata.append(ns)
print(errores_p1)
print(sum(errores_p1))

gooddata = np.array(gooddata)
mapreglas = np.zeros((len(rules.keys()), len(myticket)))
print(gooddata.shape)
i = 0
for k, regla in rules.items():
    for col in range(0,gooddata.shape[1]):
        c = gooddata[:,col]
        reglatest = ((c>=regla["r1"][0]) & (c <= regla["r1"][1])) | \
                    ((c>=regla["r2"][0]) & (c <= regla["r2"][1]))
        if reglatest.all():
            mapreglas[i, col] = 1
    i+=1
tempm = mapreglas.copy()
for i in range(mapreglas.shape[0]):
    search1 = np.sum(tempm, axis=1) == 1
    if search1.all(): 
        break
    row1 = tempm[search1, :]
    for k in range(row1.shape[0]):
        for j in range(mapreglas.shape[0]):
            if not search1[j]:
                tempm[j,:] = np.where(row1[k,:] == 1, 0, tempm[j,:])
mapdict = {}
for k, i in zip(rules.keys(), range(mapreglas.shape[0])):
    mapdict[k] = np.argmax(tempm[i,:])

print(mapdict)
result2 = 1
for k, col in mapdict.items():
    if k.startswith("depart"):
        result2 *= myticket[col]
        print(k, myticket[col])
print(result2)

