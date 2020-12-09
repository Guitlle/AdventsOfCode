with open("day5.input") as f:
    inputd = f.readlines()

test_inputd = [
    "BFFFBBFRRR\n",
    "FFFBBBFRRR\n",
    "BBFFBBFRLL\n"
]

seats = []
maxid = 0
for linea in inputd:
    binnum = linea.replace("F", "0").replace("B", "1").replace("L", "0").replace("R", "1")
    seatid = int(binnum[:-1],2)
    seats.append({
        "seatid": seatid,
        "row": seatid // 8,
        "column": seatid % 8,
        "input": linea
    })
    if seatid > maxid:
        maxid = seatid

print(maxid)
seats = sorted(seats, key = lambda x: x["seatid"])
lastid = 0
print(seats)
for s in seats:
    dx = s["seatid"]-lastid
    if dx > 1:
        print(s)
    lastid = s["seatid"]