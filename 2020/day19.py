import numpy as np

with open("day19.input") as f:
    inputd = f.readlines()

testdata = """0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4 | 4 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb"""
#inputd = testdata.split("\n")

linea = None
ix = 0
reglas = {}
while True:
    linea = inputd[ix].strip()
    if linea == "": break
    #print(linea)
    partes = linea.split(":")
    ors = partes[1].split(" | ")
    reglas[partes[0]] = [orpart.strip().split(" ") for orpart in ors]
    ix += 1
    
# Solución mala:
def checkrule_bad(regla, inputtxt, debug = False):
    if len(inputtxt) == 0:
        if debug: print("Reached end of string")
        return (False, 0)
    orparts = []
    offset = 0
    for orpart in regla:
        partstest = []
        offset = 0
        for ruleref in orpart:
            #print(ruleref)
            if "\"" in ruleref:
                partstest.append(inputtxt[0] == ruleref.strip("\""))
                offset += 1
                #print("   checkchar: ", inputtxt[0], ruleref)
            else:
                #ruleref = int(ruleref)
                #print("   checking: ", ruleref, inputtxt[i:])
                check, choffset = checkrule(reglas[ruleref], inputtxt[offset:], debug)
                partstest.append(check)
                offset += choffset
                #print("   ruleref: ", ruleref, inputtxt[i:], check)
        #print(" rulerefs: ", i, ruleref, partstest)
        orparts.append(all(partstest))
    if debug: print("orparts: ", regla, orparts, any(orparts), inputtxt, " offset", offset)
    return any(orparts), offset

# Solución correcta:
def checkrule(regla0, inputtxt, debug = False):
    checks = checktree(regla0, inputtxt, 0, debug)
    return any([check and offset == len(inputtxt) for check, offset, seq in checks])
def checktree(regla, inputtxt, offset = 0, debug = False):
    checksseq = []
    for orpart in regla:
        checksseq.extend( checkseq(orpart, inputtxt, offset, debug) )
    return checksseq
def checkseq(seq, inputtxt, offset, debug = False):
    if offset >= len(inputtxt):
        return [(False, offset, "EOF")]
    checks = [(True, offset, "__")]
    for subseq in seq:
        if "\"" in subseq:
            return [(inputtxt[offset] == subseq.strip("\""), offset+1, subseq)]
        else:
            checkstemp = []
            for check, checkoffset, sseq in checks:
                if check:
                    checkstemp.extend(checktree(reglas[subseq], inputtxt, checkoffset, debug))
                    #print(checkstemp, seq, subseq, sseq, inputtxt[choffs:])
            checks = checkstemp
    return list(filter(lambda x: x[0], checks))

ix += 1
firsttest = ix
tests = []
while ix < len(inputd):
    linea = inputd[ix].strip()
    check = checkrule(reglas["0"], linea, True)
    #tests.append(check[0] and check[1] == len(linea))
    tests.append(check)
    print(tests[-1], linea)
    #input()
    ix += 1
print(sum(tests))

# Parte 2
# Mi función original no funcionó. Tocó reescribir.
extrarules = """8: 42 | 42 8
11: 42 31 | 42 11 31"""

for linea in extrarules.split("\n"):
    linea = linea.strip()
    if linea == "": break
    partes = linea.split(":")
    ors = partes[1].split(" | ")
    reglas[partes[0]] = [orpart.strip().split(" ") for orpart in ors]
    ix += 1
#print(reglas["11"], reglas["8"])
ix = firsttest
tests = []
while ix < len(inputd):
    linea = inputd[ix].strip()
    check = checkrule(reglas["0"], linea, True)
    #tests.append(check[0] and check[1] == len(linea))
    tests.append(check)
    print(tests[-1], linea)
    #input()
    ix += 1
print(sum(tests))
