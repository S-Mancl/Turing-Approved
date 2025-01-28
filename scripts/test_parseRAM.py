# this is the minimal execution state that we must keep with the soruce code we know
state = {
    "PC": 0,
    "registers": [0,0,0,0,0,0,0,0],
    "RAM" : None
}

def readRAM():
    global state
    # read file content
    with open("given/RAM") as f:
        state["RAM"] = f.read()
    f.close()
    # get single instructions
    state["RAM"] = [''.join(state["RAM"].split(","))[16*i:16*(i+1)] for i in range(len(state["RAM"].split(","))//16)][1:]

def simulate():
    global state
    # opcodes
    translations = {
        "0001": add,
        "0101": unused,
        "0000": jump,
        "0100": unused,
        "1100": unused,
        "0010": load,
        "1010": unused,
        "0110": unused,
        "1110": unused,
        "1001": unused,
        "1101": unused,
        "1000": unused,
        "0011": store,
        "1011": unused,
        "0111": unused,
        "1111": trap
    }
    while state["PC"] != len(state["RAM"]):
        curr_instruction = state["RAM"][state["PC"]]
        translations[curr_instruction[:4]](curr_instruction[4:])
    print()

def unused(data):
    # this instruction is unused
    pass

def add(data):
    # the sum is always R0, R1, R2
    global state
    state["registers"][0] = state["registers"][1] + state["registers"][2]
    # we print it immediately to avoid reading the memory dump
    print(chr(state["registers"][0]),end='')
    # next instruction
    state["PC"] += 1

def jump(data):
    global state
    addr = int(data[3:],2)
    if addr:
        state["PC"] = addr
    else:
        state["PC"] += 1

def load(data):
    global state
    DR = int(data[:3],2)
    addr = int(data[3:],2)
    state["registers"][DR] = int(state["RAM"][addr],2)
    state["PC"] += 1

def store(data):
    # we don't really need to implement this one
    global state
    state["PC"] += 1

def trap(data):
    # the TRAP instruction is creating us a lot of problems, so lets just skip it
    global state
    state["PC"] += 1

def print_state():
    global state
    print("PC: {PC} R0: {R0} R1: {R1} R2: {R2}".format(PC=state["PC"],R0=state["registers"][0],R1=state["registers"][1],R2=state["registers"][2]))

if __name__ == "__main__":
    readRAM()  # setup
    simulate() # run
