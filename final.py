# Harin Ponna
# Final Project
# Fantasy Hockey Statistics

from finalLib import *
from tabulate import tabulate
from matplotlib import pyplot


skt = []
with open('skaterStats.csv') as f:
    for i, line in enumerate(f):
        if i == 0:
            sCategories = line.strip()
            sCategories = sCategories.split(',')
            sCategories.append('Fantasy Points')
            sCategories.append('Fantasy Points/Game')
        else:
            s = line.strip()
            s = s.split(',')
            s = skater(s[0], s[1], s[2], s[3], s[4], s[5], s[6], s[7], s[8], s[9],
                       s[10], s[11], s[12], s[13], s[14], s[15], s[16])
            skt.append(s.getStats())

skaterRef = ['name', 'team', 'pos', 'games', 'g', 'a', 'pts', 'plusminus', 'pim', 'sog', 'gwg', 'ppg', 'ppa', 'shg', 'sha', 'hits', 'bs', 'fPts', 'avg']

filters = ['All', 'FWD', 'C', 'RW', 'LW', 'D']

gls = []
with open('goalieStats.csv') as f:
    for i, line in enumerate(f):
        if i == 0:
            gCategories = line.strip()
            gCategories = gCategories.split(',')
            gCategories.append('Fantasy Points')
            gCategories.append('Fantasy Points/Game')
        else:
            g = line.strip()
            g = g.split(',')
            g = goalie(g[0], g[1], g[2], g[3], g[4], g[5], g[6], g[7], g[8], g[9], g[10], g[11])
            gls.append(g.getStats())

goalieRef = ['name', 'team', 'games', 'w', 'l', 'otl', 'gaa', 'ga', 'sa', 'sv', 'pct', 'so', 'fPts', 'avg']

playerType = ['Skaters', 'Goalies']

while True:
    print('Skaters or Goalies?')
    typeNum = choice(playerType)
    if typeNum == 0:
        print('Filter by Position')
        posFilter = choice(filters)
        if posFilter == 0:
            print('What Stat Would You Like to Sort By?')
            statNum = choice(sCategories)
            finalTable = top30(skt, skaterRef[statNum])
            categories = sCategories
            break
        elif posFilter == 1:
            filtSkt = []
            for i in skt:
                if i['pos'] == 'C' or i['pos'] == 'LW' or i['pos'] == 'RW':
                    filtSkt.append(i)
            print('What Stat Would You Like to Sort By?')
            statNum = choice(sCategories)
            finalTable = top30(filtSkt, skaterRef[statNum])
            categories = sCategories
            break
        elif posFilter == 2:
            filtSkt = []
            for i in skt:
                if i['pos'] == 'C':
                    filtSkt.append(i)
            print('What Stat Would You Like to Sort By?')
            statNum = choice(sCategories)
            finalTable = top30(filtSkt, skaterRef[statNum])
            categories = sCategories
            break
        elif posFilter == 3:
            filtSkt = []
            for i in skt:
                if i['pos'] == 'RW':
                    filtSkt.append(i)
            print('What Stat Would You Like to Sort By?')
            statNum = choice(sCategories)
            finalTable = top30(filtSkt, skaterRef[statNum])
            categories = sCategories
            break
        elif posFilter == 4:
            filtSkt = []
            for i in skt:
                if i['pos'] == 'LW':
                    filtSkt.append(i)
            print('What Stat Would You Like to Sort By?')
            statNum = choice(sCategories)
            finalTable = top50(filtSkt, skaterRef[statNum])
            categories = sCategories
            break
        elif posFilter == 5:
            filtSkt = []
            for i in skt:
                if i['pos'] == 'D':
                    filtSkt.append(i)
            print('What Stat Would You Like to Sort By?')
            statNum = choice(sCategories)
            finalTable = top30(filtSkt, skaterRef[statNum])
            categories = sCategories
            break
    elif typeNum == 1:
        print('What Stat Would You Like to Sort By?')
        statNum = choice(gCategories)
        finalTable = top30(gls, goalieRef[statNum])
        categories = gCategories
        break

f = open('table.txt', 'w')
f.write(tabulate(finalTable, headers=categories))
f.close()

x = []
y = []
for i in range(len(finalTable)):
    x.append(i+1)
    y.append(finalTable[i][statNum])
pyplot.bar(x, y)
for i in range(len(x)):
    pyplot.text(x[i], y[i]*0.6, finalTable[i][0], rotation=90, verticalalignment='center', horizontalalignment='center')
pyplot.xlabel('Rank')
pyplot.ylabel(categories[statNum])
pyplot.title('Rankings by '+categories[statNum])
pyplot.savefig('bar.png')
pyplot.show()



if len(categories) == len(sCategories):
    if 3 <= statNum <= 16:
        scatterx = []
        scattery = []
        for i in range(len(finalTable)):
            scatterx.append(finalTable[i][statNum])
            scattery.append(finalTable[i][-2])
        pyplot.scatter(scatterx, scattery)
        pyplot.xlabel(categories[statNum])
        pyplot.ylabel(categories[-2])
        pyplot.title('Correlation Between '+categories[statNum]+' and '+categories[-2])
        pyplot.savefig('scatter.png')
        pyplot.show()

if len(categories) == len(gCategories):
    if 3 <= statNum <= 11:
        scatterx = []
        scattery = []
        for i in range(len(finalTable)):
            scatterx.append(finalTable[i][statNum])
            scattery.append(finalTable[i][-2])
        pyplot.scatter(scatterx, scattery)
        pyplot.xlabel(categories[statNum])
        pyplot.ylabel(categories[-2])
        pyplot.title('Correlation Between '+categories[statNum]+' and '+categories[-2])
        pyplot.savefig('scatter.png')
        pyplot.show()
