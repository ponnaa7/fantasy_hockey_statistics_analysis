# Harin Ponna
# Final Project Library
# Fantasy Hockey Statistics

class player():

    def __init__(self, name, team):
        self.name = name
        self.team = team

    def getStats(self):
        pass

class skater(player):

    def __init__(self, name, team, pos, games, g, a, pts, plusminus, pim, sog, gwg, ppg, ppa, shg, sha, hits, bs):
        player.__init__(self, name , team)
        self.pos = pos
        self.games = int(games)
        self.g = int(g)
        self.a = int(a)
        self.pts = int(pts)
        self.plusminus = int(plusminus)
        self.pim = int(pim)
        self.sog = int(sog)
        self.gwg = int(gwg)
        self.ppg = int(ppg)
        self.ppa = int(ppa)
        self.shg = int(shg)
        self.sha = int(sha)
        self.hits = int(hits)
        self.bs = int(bs)

    def getStats(self):
        info = dict(
            name = self.name,
            team = self.team,
            pos = self.pos,
            games = self.games,
            g = self.g,
            a = self.a,
            pts = self.pts,
            plusminus = self.plusminus,
            pim = self.pim,
            sog = self.sog,
            gwg = self.gwg,
            ppg = self.ppg,
            ppa = self.ppa,
            shg = self.shg,
            sha = self.sha,
            hits = self.hits,
            bs = self.bs,
            fPts = round((self.g*2)+(self.a)+((self.ppg+self.ppa)*0.5)+((self.shg+self.sha)*0.5)+(self.sog*0.1)+(self.hits*0.1)+(self.bs*0.5), 2),
            avg = round(((self.g*2)+(self.a)+((self.ppg+self.ppa)*0.5)+((self.shg+self.sha)*0.5)+(self.sog*0.1)+(self.hits*0.1)+(self.bs*0.5))/self.games, 2)
            )
        return info

class goalie(player):

    def __init__(self, name, team, games, w, l, otl, gaa, ga, sa, sv, pct, so):
        player.__init__(self, name , team)
        self.games = int(games)
        self.w = int(w)
        self.l = int(l)
        self.otl = int(otl)
        self.gaa = float(gaa)
        self.ga = int(ga)
        self.sa = int(sa)
        self.sv = int(sv)
        self.pct = float(pct)
        self.so = int(so)

    def getStats(self):
        info = dict(
            name = self.name,
            team = self.team,
            games = self.games,
            w = self.w,
            l = self.l,
            otl = self.otl,
            gaa = self.gaa,
            ga = self.ga,
            sa = self.sa,
            sv = self.sv,
            pct = self.pct,
            so = self.so,
            fPts = round((self.w*4)+(self.ga*(-2))+(self.sv*0.2)+(self.so*3)+(self.otl), 2),
            avg = round(((self.w*4)+(self.ga*(-2))+(self.sv*0.2)+(self.so*3)+(self.otl))/self.games, 2)
            )
        return info

def top30(table, stat):
    sortedTable = sorted(table, key=lambda x: x[stat], reverse=True)
    t30 = []
    for i in range(30):
        info = list(sortedTable[i].values())
        t30.append(info)
    return t30

def choice(lis):
    for i, option in enumerate(lis):
        print(str(i+1)+':', option)
    while True:
        c = input('Enter the Number: ')
        if 1 <= int(c) <= len(lis):
            return int(c)-1
        else:
            print('Invalid Input')
    
    

    
    
    
        
        
        
