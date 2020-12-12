import numpy as np

with open("day12.input") as f:
    inputd = f.readlines()

testdata = """F10
N3
F7
R90
F11"""
#inputd = testdata.split("\n")

pos = [0,0]
dxdy = [1,0]
instrs = {
    "N": (0,1),
    "S": (0,-1),
    "E": (1,0),
    "W": (-1,0)
}
for l in inputd:
    n = int(l[1:])
    if l[0] in instrs:
        pos[0] += instrs[l[0]][0]*n
        pos[1] += instrs[l[0]][1]*n
    if l[0] == "R":
        theta = np.radians(-n)
        c, s = np.cos(theta), np.sin(theta)
        R = np.array(((c, -s), (s, c)))
        dxdy = np.matmul(R, dxdy)
    if l[0] == "L":
        theta = np.radians(n)
        c, s = np.cos(theta), np.sin(theta)
        R = np.array(((c, -s), (s, c)))
        dxdy = np.matmul(R, dxdy)
    if l[0] == "F":
        pos[0] += dxdy[0]*n
        pos[1] += dxdy[1]*n
    #print(pos)
print(pos, ", d = ", np.sum(np.abs(pos)))

# Segunda parte
pos = [0,0]
wpoint = [10,1]
dxdy = [1,0]
instrs = {
    "N": (0,1),
    "S": (0,-1),
    "E": (1,0),
    "W": (-1,0)
}
for l in inputd:
    n = int(l[1:])
    if l[0] in instrs:
        wpoint[0] += instrs[l[0]][0]*n
        wpoint[1] += instrs[l[0]][1]*n
    if l[0] == "R":
        theta = np.radians(-n)
        c, s = np.cos(theta), np.sin(theta)
        R = np.array(((c, -s), (s, c)))
        #dxdy = np.matmul(R, dxdy)
        wpoint = np.matmul(R, wpoint)
    if l[0] == "L":
        theta = np.radians(n)
        c, s = np.cos(theta), np.sin(theta)
        R = np.array(((c, -s), (s, c)))
        wpoint = np.matmul(R, wpoint)
    if l[0] == "F":
        pos[0] += wpoint[0]*n
        pos[1] += wpoint[1]*n
    #print(pos)
print(pos, ", d = ", np.sum(np.abs(pos)))