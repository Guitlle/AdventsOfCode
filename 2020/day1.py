with open("day1.input") as f:
  input = []
  for l in f.readlines():
    input.append(int(l.strip()))
resp = -1
for i,x in enumerate(input):
  for j in range(i, len(input)):
    if x+input[j] == 2020:
      resp = x*input[j]
      break
  if resp != -1:
    break
print(resp)
resp = -1
for i,x in enumerate(input):
  for j in range(i, len(input)):
    for k in range(j, len(input)):    
      if x+input[j]+input[k] == 2020:
        resp = x*input[j]*input[k]
        break
    if resp != -1:
      break
  if resp != -1:
    break
print(resp)
