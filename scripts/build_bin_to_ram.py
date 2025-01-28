with open("program.bin") as f:
    data = f.read()
f.close()

with open("given/RAM","w") as f:
    f.write(','.join(list(''.join(data.split('\n')))))
f.close()

print("> RAM ready")
