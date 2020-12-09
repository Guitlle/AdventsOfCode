with open("day8.input") as f:
    inputd = f.readlines()

execlines = {}
cline = 0
reg = 0
while True:
    if cline not in execlines:
        execlines[cline] = 1
    else:
        break
    instr = str.split(inputd[cline], " ")
    command = instr[0] 
    param = int(instr[1])
    if command == "jmp":
        cline += param
        continue
    elif command == "acc":
        reg += param
    
    cline += 1

print(reg)

execlines = {}
cline = 0
reg = 0
jmpnops = []
first = True
currentTest = None
nlines = len(inputd)
while True:
    if cline not in execlines and cline >= 0 and cline < nlines:
        execlines[cline] = 1
    else:
        print("**\t", cline, reg)
        if input("Enter q to quit") == "q":
            break
        first = False
        execlines = {}
        cline = 0
        reg = 0        
        if currentTest is not None:    
            inputd[currentTest["line"]] = inputd[currentTest["line"]].replace(
                "nop" if currentTest["command"]=="jmp" else "jmp",
                currentTest["command"]
            )
        if currentTest is not None:
            print(inputd[currentTest["line"]])
        currentTest = jmpnops.pop()
        print(inputd[currentTest["line"]])
        inputd[currentTest["line"]] = inputd[currentTest["line"]].replace(
                        currentTest["command"],
                        "nop" if currentTest["command"]=="jmp" else "jmp"
                    )
        print(inputd[currentTest["line"]])
        continue
    instr = str.split(inputd[cline], " ")
    command = instr[0] 
    param = int(instr[1])
    if command == "jmp":
        if first:
            jmpnops.append({
                "line": cline, 
                "command": instr[0], 
                "param": instr[1],
                "test": False
            })
        cline += param
        continue
    elif command == "acc":
        reg += param
    elif command == "nop":
        if first:
            jmpnops.append({
                "line": cline, 
                "command": instr[0], 
                "param": instr[1],
                "test": False
            })
    cline += 1
    if cline >= len(inputd):
        break
