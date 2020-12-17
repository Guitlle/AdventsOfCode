import numpy as np

with open("day17.input") as f:
    inputd = f.readlines()

data = np.array([[1 if y=="#" else 0 for y in list(x.strip())]\
                     for x in inputd])
data = data.reshape([data.shape[0], data.shape[1], -1])

kernel = np.ones([3,3,3])
kernel[1,1,1] = 0

newdata = np.zeros([x + 8*2 for x in data.shape])

print(newdata.shape)

newdata[8:data.shape[0]+8, 8:data.shape[1]+8, 8:data.shape[2]+8] = data

print(newdata[0:18,0:18,8])

for n in range(0,6):
    tempdata = newdata.copy()
    for x in range(1,newdata.shape[0]-1):
        for y in range(1,newdata.shape[1]-1):
            for z in range(1,newdata.shape[2]-1):
                conv = newdata[x-1:x+2, y-1:y+2, z-1:z+2] * kernel
                suma = conv.flatten().sum()
                if suma not in [2,3] and newdata[x,y,z] == 1:
                    tempdata[x,y,z] = 0
                elif newdata[x,y,z] == 0 and suma == 3:
                    tempdata[x,y,z] = 1
               # if z == 8 and x > 8-1 and x < 8+2:
                    #print(x,y,z, conv, suma)
                    #input()
    print("***", n)
    print(tempdata[0:18,0:18,8])
    newdata = tempdata
print(newdata[0:18,0:18,8])
print(newdata.flatten().sum())

# Parte 2

data = data.reshape([data.shape[0], data.shape[1], 1, 1])

kernel = np.ones([3,3,3,3])
kernel[1,1,1,1] = 0

newdata = np.zeros([x + 8*2 for x in data.shape])

print(newdata.shape)

newdata[8:data.shape[0]+8, 8:data.shape[1]+8, 8:data.shape[2]+8, 8:data.shape[3]+8] = data

for n in range(0,6):
    tempdata = newdata.copy()
    for x in range(1,newdata.shape[0]-1):
        for y in range(1,newdata.shape[1]-1):
            for z in range(1,newdata.shape[2]-1):
                for w in range(1,newdata.shape[3]-1):
                    conv = newdata[x-1:x+2, y-1:y+2, z-1:z+2, w-1:w+2] * kernel
                    suma = conv.flatten().sum()
                    if suma not in [2,3] and newdata[x,y,z,w] == 1:
                        tempdata[x,y,z,w] = 0
                    elif newdata[x,y,z,w] == 0 and suma == 3:
                        tempdata[x,y,z,w] = 1
                   # if z == 8 and x > 8-1 and x < 8+2:
                    #print(x,y,z, conv, suma)
                    #input()
    newdata = tempdata
print(newdata.flatten().sum())