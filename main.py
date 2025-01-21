import json
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import r2_score

COEFFIFCIENTS = {
    "Data": 1.506849315 ,
    "Market":4.074074074,
    "Research": 3.055555556 ,
    "Tools":3.333333333
}

DIFFICULTY_COEFFICENTS = {
    "Data": 1.4,
    "Market": 1,
    "Research": 1.5,
    "Tools": 1.3
}

# FUNCTIONS

def get_cost(type, level):
    '''Returns the adjusted number of the upgrade based off the mining operation upgrades.'''
    return COEFFIFCIENTS[type] * level

ores = []
oreCost = []
oreNumbers = []
upgradeInfo = json.load(open('upgrades.json'))

for i, upgradeList in upgradeInfo.items():
    for key,value in upgradeList.items():
        if key not in ores:
            ores.append(key)

fig, ax = plt.subplots()
getOre = input('Enter ore: ')

for i, upgradeList in upgradeInfo.items():
    for key,value in upgradeList.items():
        if key == getOre:
            ax.bar(int(i), value, label=i, color='gray')
            oreCost.append(value)
            oreNumbers.append(int(i))
ax.set_title(f'Upgrade Costs for {getOre}')
ax.set_xlabel('Upgrade')
ax.set_ylabel('Cost')

print(f"Mean: {np.mean(oreCost):.3f}")
print(f"Median: {np.median(oreCost)}")
print(f"Sum: {np.sum(oreCost)}")
print(f"Min: {np.min(oreCost)}")
print(f"Max: {np.max(oreCost)}")
print(f"Standard Deviation: {np.std(oreCost):.3f}")

model = np.poly1d(np.polyfit(oreNumbers, oreCost, 2))
line = np.linspace(min(oreNumbers), max(oreNumbers),200)

print(f"R^2 value: {r2_score(oreCost, model(oreNumbers)):.3f}")

ax.plot(line, model(line), label='Trendline', color='red')
#plt.show()

while True:
    level = input('Enter upgrade and level: ')
    split = level.split(" ")
    newCost = get_cost(split[0], int(split[1]))
    realCost = model(newCost) * DIFFICULTY_COEFFICENTS[split[0]] 
    realCost -= realCost % 5
    print(f"Cost: {realCost:.0f} {getOre}.")
