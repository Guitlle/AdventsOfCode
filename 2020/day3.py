import sys

with open("day3.input") as f:
  input =  f.readlines()


dxdy = (int(sys.argv[1]), int(sys.argv[2]))
print(dxdy)
pos  = [0,0]
arboles = 0
w = len(input[0])-1
while pos[1] < len(input):
  if input[pos[1]][pos[0]%w] == "#":
    arboles += 1
  pos[0] += dxdy[0]
  pos[1] += dxdy[1]

print(arboles)
