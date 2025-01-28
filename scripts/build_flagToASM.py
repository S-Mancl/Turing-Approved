from random import randrange,choice,shuffle


def composeJump(index):
    return choice([
        "BRNZP start_{nxt}".format(nxt=str(index+1))#,
#        """LEA R7, start_{nxt}
#RET""".format(nxt=str(index+1)),
#        "JSR start_{nxt}".format(nxt=str(index+1))
        ])
    pass

def composePart(index,char):
    n = ord(char)
    data1 = randrange(1,n)
    data2 = n - data1
    return [
        "data{i}_1 .fill {data1}".format(i=str(index),data1=str(data1)),
        "data{i}_2 .fill {data2}".format(i=str(index),data2=str(data2)),
        """start_{i} LD R2, data{i}_1
LD R1, data{i}_2
ADD R0, R1, R2
ST R0, data{i}_2
TRAP x25 ; EVIL INSTR DO NOT DECOMMENT
{JMP}""".format(i=str(index),JMP=composeJump(index))
    ]

with open("flag.txt") as f:
    flag = f.read()[:-1]
f.close()

instructions = []
for i in range(0,len(flag)):
    instructions = instructions + composePart(i,flag[i])

shuffle(instructions)
shuffle(instructions)
shuffle(instructions)

txt = """.ORIG 0
BRNZP start_0
"""
for line in instructions:
    txt = txt + line + '\n'
txt = txt + "start_{i} TRAP x25\n.END".format(i=len(flag))

with open("program.asm","w") as f:
    f.write(txt)
f.close()

print("> program.asm created")
