import json

addToUpgrade = False
miningUpgrades = open("tccMiningUpgrades.txt","r")
table = {}
current = 1

with miningUpgrades as file:
    for i,line in enumerate(file):
        lineText = line.strip()
        if not addToUpgrade:
            try:
                upgrade = int(lineText)
                assert(upgrade == current) 

                current += 1
                table[upgrade] = {}
                addToUpgrade = True
            except:
                continue
        else:
            if lineText == "}}":
                addToUpgrade = False
            elif lineText == "":
                continue
            else:
                upgrade = lineText.split("*")
                table[current - 1][upgrade[0].strip()] = int(upgrade[1].strip())
                


with open("tccUpgrades.json","w") as file:
    json.dump(table,file,indent=4)