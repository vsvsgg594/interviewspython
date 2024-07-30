odict = {}
for i in range(4):
    idict = {}
    for j in range(4):
        idict[j] = j**2
    odict[i] = idict
print(odict)