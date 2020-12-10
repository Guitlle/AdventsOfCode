import pandas as pd

with open("day10.input") as f:
    inputd = f.readlines()

testdata = """28,33,18,42,31,14,46,20,48,47,24,23,49,45,19,38,39,11,1,32,25,35,8,17,7,9,4,2,34,10,3"""

#inputd = testdata.split("\n")
data = [int(linea) for linea in inputd]
data.append(0)
sortdata = sorted(data)
sortdata.append(sortdata[-1]+3)

result = pd.Series(sortdata).diff().value_counts()
#print(result)
print(result.values[0]*result.values[1])


# Este método funcionó con pocos datos pero al analizar el input grande tomó demasiado tiempo
# Tras media hora de ejecución, aún no termina.
if False:
    def rec_countcombs(partialdata):
        n0 = partialdata[0]
        opciones = 0
        if len(partialdata) >= 2 and partialdata[1]-n0<=3:
            opciones += rec_countcombs(partialdata[1:])
        if len(partialdata) >= 3 and partialdata[2]-n0<=3:
                opciones += rec_countcombs(partialdata[2:])
        if len(partialdata) >= 4 and partialdata[3]-n0<=3:
                opciones += rec_countcombs(partialdata[3:])
        if len(partialdata) == 1:
            opciones = 1
        #print(opciones, partialdata)
        return opciones

    print(rec_countcombs(sortdata))

# Probando otro método que no sea recursivo
# Agrupar unos continuos para hacer combinatoria
c1 = 0
prev = 0
cont1s = []
diffs = pd.Series(sortdata).diff().values
for n in diffs:
    if n==1:
        c1 += 1
    else:
        cont1s.append(c1)
        c1 = 0
    prev = n
result2 = 1

# Parece que sólo se tienen grupos de 2, 3 y 4 unos continuos
# Cada uno de esos casos multiplica las combinaciones posibles por
# 2, 4 y 7 respectivamente.
for k, n in pd.Series(cont1s).value_counts().iteritems():
    if k == 2:
        result2 *= 2**n
    elif k == 3:
        result2 *=4**n
    elif k == 4:
        result2 *=7**n
    #print(k,n, result2)
print(result2)
