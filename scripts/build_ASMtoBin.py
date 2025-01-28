labels = {}

def learn_label_positions(program):
    global labels
    for i in range(len(program)):
        line = program[i]
        if line.startswith("data") or line.startswith("start"):
            labels[line.split(" ")[0]] = i-1

def translate(i, program):
    if program[i].startswith(".ORIG"):
        return "0000000000000000"
    elif program[i].startswith("TRAP"):
        return "1111000000100101"
    elif program[i].startswith("ADD"):
        return "0001000001000010"
    elif program[i].startswith("BRNZP"):
        myLabel = program[i].split(" ")[1]
        myAddress = bin(labels[myLabel])[2:]
        return "0000111" + "0"*(9-len(myAddress)) + myAddress
    elif program[i].startswith("LD"):
        myLabel = program[i].split(" ")[2]
        myAddress = bin(labels[myLabel])[2:]
        return "0010001" + "0"*(9-len(myAddress)) + myAddress
    elif program[i].startswith("data"):
        value = bin(int(program[i].split(" ")[2]))[2:]
        return "0"*(16-len(value)) + value
    elif program[i].startswith("start") and not "TRAP" in program[i]: # LD
        myLabel = program[i].split(" ")[3]
        myAddress = bin(labels[myLabel])[2:]
        return "0010010" + "0"*(9-len(myAddress)) + myAddress
    elif program[i].startswith("start"):
        return "1111000000100101"
    elif program[i].startswith("ST"):
        myLabel = program[i].split(" ")[2]
        myAddress = bin(labels[myLabel])[2:]
        return "0011000" + "0"*(9-len(myAddress)) + myAddress

with open("program.asm") as f:
    program = f.read().split("\n")[:-1]
f.close()

learn_label_positions(program)

for i in range(len(program)):
    program[i] = translate(i,program)

with open("program.bin",'w') as f:
    f.write('\n'.join(program))
f.close()

print("> assembled successfully")
