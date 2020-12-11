with open("day11.input") as f:
    inputd = f.readlines()

testdata = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""

#inputd = [x.strip() for x in testdata.split("\n")]
inputd = [x.strip() for x  in inputd]
nrows = len(inputd)
ncols = len(inputd[0])
def isempty(x):
    return x == "L" # or x=="."
def isfloor(x):
    return x == "."
def countSeats(inputd):
    c = 0
    for i in range(nrows):
        for j in range(ncols):
            if inputd[i][j] == "#":
                c+=1
    return c

def ronda(inputd):
    newdata = []                
    for i in range(nrows):
        newrow = list(inputd[i])
        for j in range(ncols):
            adjacent = [(i+1,j), (i-1,j), (i+1,j+1), (i-1,j+1),
            (i+1,j-1), (i-1,j-1), (i,j+1), (i,j-1)]
            adjdata = [inputd[y][x] for y,x in adjacent if x>=0 and y>=0 and y<nrows and x<ncols]
            nempties = [not isempty(inputd[y][x]) for y,x in adjacent if x>=0 and y>=0 and y<nrows and x<ncols and not isfloor(inputd[y][x])]
            floor = isfloor(inputd[i][j])
            if floor:
                continue
            #print(inputd[i][j], i,j, adjdata,nempties)
            if sum(nempties) >= 4:
                newrow[j] = "L"
            elif sum(nempties) == 0:
                newrow[j] = "#"
        newdata.append(newrow)
    return newdata

r1 = [list(x) for x in inputd]
prev = 0
n = 0
while True:
    r1 = ronda(r1)
    prev = n    
    n = countSeats(r1)
    if prev == n:
        break
print(prev)

# Segunda parte
def goodxy(x,y):
    return x>=0 and y>=0 and y<nrows and x<ncols
def rondaB(inputd):
    newdata = []                
    for i in range(nrows):
        newrow = list(inputd[i])
        for j in range(ncols):
            floor = isfloor(inputd[i][j])
            if floor:
                continue
            #adjacent = [(i+1,j), (i-1,j), (i+1,j+1), (i-1,j+1),
            #(i+1,j-1), (i-1,j-1), (i,j+1), (i,j-1)]
            adjdata = []
            for dx,dy in [
                (1,0), (0,1), (-1,0), (0,-1), (1,1), (1,-1), (-1,1), (-1,-1), 
            ]:
                x = j
                y = i
                while goodxy(x+dx, y+dy):
                    datum = inputd[y+dy][x+dx]
                    if datum in ["#", "L"]:
                        adjdata.append(datum)
                        break
                    x += dx
                    y += dy
            nempties = [x == "#" for x in adjdata if x != "."]

            #print(inputd[i][j], i,j, adjdata,nempties)
            if sum(nempties) >= 5:
                newrow[j] = "L"
            elif sum(nempties) == 0:
                newrow[j] = "#"
        newdata.append(newrow)
    return newdata

r1 = [list(x) for x in inputd]
prev = 0
n = 0
while True:
    r1 = rondaB(r1)
    prev = n    
    n = countSeats(r1)
    print(n)
    if prev == n:
        break
print(prev)
