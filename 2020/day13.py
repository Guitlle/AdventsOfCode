import numpy as np

with open("day13.input") as f:
    inputd = f.readlines()

testdata = """939
7,13,x,x,59,x,31,19"""
#inputd = testdata.split("\n")

minn = int(inputd[0])
ns = [int(x) for x in  inputd[1].split(",") if x !="x"]

print(ns)

found = False
for i in range(minn, minn + max(ns)):
    for n in ns:
        if i%n == 0:
            found = True
            break
    if found:
        break
if found:
    print(i, n, i-minn, (i-minn)*n )

# Segunda parte

if False:
    testdata = """939
    17,x,13,19"""
    inputd = testdata.split("\n")
    minn = int(inputd[0])
    ns = [int(x) if x != "x" else -1 for x in  inputd[1].split(",")]
    print(ns)
    maxn = max(ns)
    argmaxn = np.argmax(ns)
    start = 1e14
    i = (start//maxn)*maxn + argmaxn
    print(argmaxn, maxn)
    while True:
        checks = [(i+ix-argmaxn*2)%n == 0 for ix,n in enumerate(ns) if n >-1]
        print(i, checks)
        #input("")
        if all(checks):
            break
        i += maxn
    print(i-argmaxn*2)

from functools import reduce

if False:
    testdata = """939
    17,x,13,19"""
    #inputd = testdata.split("\n")
    ns = [int(x) if x != "x" else -1 for x in  inputd[1].split(",")]
    maxn = max(ns)
    argmaxn = np.argmax(ns)
    i = ns[0] # 100080093590198# (1e14//ns[0]) * ns[0]
    ab = ns[0] * maxn
    print(argmaxn, maxn)
    while True:
        i += ns[0]
        if i*(i+argmaxn) % ab == 0:
            mulns = reduce(lambda x,y: x*y, [n for n in ns if n > 0])
            mulxs = reduce(lambda x,y: x*y, [i+j for j,n in enumerate(ns) if n > 0])
            #print(ns, mulns, mulxs, [i+j for j,n in enumerate(ns) if n > 0])
            #input(i)

            if mulxs % mulns == 0:
                checks = [(i+ix)%n == 0 for ix,n in enumerate(ns) if n >-1]
                print(i, checks)
                #input("")
                if all(checks):
                    break
    print(i)

testdata = """939
67,7,x,59,61"""
#inputd = testdata.split("\n")
ns = [int(x) if x != "x" else -1 for x in  inputd[1].split(",")]
mulns = reduce(lambda x,y: x*y, [n for n in ns if n > 0])
print(mulns)
maxn = max(ns)
argmaxn = np.argmax(ns)
i = float(mulns) # 100080093590198# (1e14//ns[0]) * ns[0]
ab = ns[0] * maxn
print(argmaxn, maxn)
while True:
    i -= ns[0]
    if i*(i+argmaxn) % ab == 0:
        checks = [(i+ix)%n == 0 for ix,n in enumerate(ns) if n >-1]
        print(i, checks)
        #input("")
        if all(checks):
            break
print(i)