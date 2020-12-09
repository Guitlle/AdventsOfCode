import re
import numpy as np
import pandas as pd

with open("day7.input") as f:
    inputd = f.readlines()

testdata = """shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.""".split("\n")
#inputd = testdata

# light red bags contain 1 bright white bag, 2 muted yellow bags.
data = []
for linea in inputd:
    key = re.findall("(\w+ \w+) bags contain", linea)[0]
    values = re.findall("(\d+) (\w+ \w+) bags?[\,\.\s]", linea)
    for n, val in values:
        data.append([key, val, n])

df = pd.DataFrame(data = data, columns = ["to", "from", "n"])
df["n"] = df.n.astype(int)
df = df.pivot("to", "from", "n")
reindexer = list(set(df.columns).union(set(df.index)))
df = df.reindex(columns=reindexer, index=reindexer).fillna(0)

invec = pd.Series(np.zeros([len(df)]), index=df.index)
invec.loc["shiny gold"] = 1

output = set()

for i in range(len(df)):
    outvec = np.matmul(invec, df.values.T)
    invec = np.where(outvec>0, 1, 0)
    output = output.union(set(df.index[outvec > 0]))

print(len(output))

# Segunda parte

invec = pd.Series(np.zeros([len(df)]), index=df.index)
invec.loc["shiny gold"] = 1

total = 0
for i in range(len(df)):
    outvec = np.matmul(invec, df.values)
    total += np.sum(outvec)
    invec = np.copy(outvec)
    
print(total)