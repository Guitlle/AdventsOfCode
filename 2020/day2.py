import re

with open("day2.input") as f:
  input =  f.readlines()

valid = 0
for i in input:
  rule = re.findall("^(\d+)\-(\d+)\s+(\w)\: (\w+)", i)[0]
  #search = re.findall(rule[2]+"{"+rule[0]+","+rule[1]+"}", rule[3])
  minn = int(rule[0])
  maxn = int(rule[1])
  n = sum([c==rule[2] for c in rule[3]])
  if n >= minn and n <=maxn:
    valid+=1

print(valid)

valid = 0
for i in input:
  rule = re.findall("^(\d+)\-(\d+)\s+(\w)\: (\w+)", i)[0]
  #search = re.findall(rule[2]+"{"+rule[0]+","+rule[1]+"}", rule[3])
  i1 = int(rule[0])
  i2 = int(rule[1])
  if (rule[3][i1-1] == rule[2]) != \
      (rule[3][i2-1] == rule[2]):
    valid+=1
    

print(valid)
