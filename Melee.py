from operator import neg
from turtle import pos


class MeleeWeapon:
    '''
    The Melee Weapon Class is an object of type Melee,
    which stores information about a melee weapon    
    '''
    def __init__(self, name, type, dmg, range, speed, cd, cc, sc, dispo, ft):
        self.name = name
        self.type = type
        self.dmg = dmg
        self.range = range
        self.speed = speed
        self.cd = cd
        self.cc = cc
        self.sc = sc
        self.dispo = dispo
        self.ft = ft

class MeleeBuild:
    '''
    The Melee Build Class is an object of type Build,
    which stores the build of the set of mods
    '''
    def __init__(self, mods, rivenSettings, otherSettings):
        self.br = mods['Blood Rush'] * 4.4
        self.ss = mods['Sacrificial Steel'] * 2.2
        self.os = mods['Organ Shatter'] * 0.9
        self.gm1 = mods['Gladiator Might'] * 0.6 # cd
        self.gm2 = mods['Gladiator Might'] * 1.1 # cc
        self.co = mods['Condition Overload'] * 0.8 * otherSettings['Procs']
        self.ppp = mods['Primed Pressure Point'] * 1.65
        self.pf = mods['Primed Fury'] * 0.55
        self.bf = mods['Berserker Fury'] * 0.7
        self.pr = mods['Primed Reach'] * 3
        self.slb = mods['Spring-Loaded Blade'] * 2
        self.ww = mods['Weeping Wounds'] * 4.4
        self.vs = mods['Virulent Scourge'] * 0.6# - otherSettings['Unranked Viral' * 0.45] # Both tox and sc
        self.vf = mods['Vicious Frost'] * 0.6# - otherSettings['Unranked Viral' * 0.45] # Both cold and sc
        self.cm1 = mods['Carnis Mandible'] * 0.9 # slash
        self.cm2 = mods['Carnis Mandible'] * 0.6  # sc
        self.b = mods['Bane'] * 0.55
        self.ars = otherSettings['Arcane Strike'] * 0.6
        self.arf = otherSettings['Arcane Fury'] * 1.8
        self.riven = {
            'cc': mods['Riven'] * rivenSettings['+Critical Chance'] * 1.485,
            'cd': mods['Riven'] * rivenSettings['+Critical Damage'] * 0.743,
            'as': mods['Riven'] * rivenSettings['+Attack Speed'] * 0.453,
            'rng': mods['Riven'] * rivenSettings['+Range'] * 1.6,
            'bane': mods['Riven'] * rivenSettings['+Bane'] * 0.371,
            'dmg': mods['Riven'] * rivenSettings['+Melee Damage'] * 1.359,
            '-h': mods['Riven'] * rivenSettings['-Harmless'] * -1,
            '-p': mods['Riven'] * rivenSettings['-Puncture'] * -0.988,
            '-i': mods['Riven'] * rivenSettings['-Impact'] * -0.988,
        }

        if mods['Riven'] == 1:
            self.balanceRiven()


    
    def balanceRiven(self):
        numPos = 0
        numNeg = 0
        posMulti = 1
        negMulti = 1

        for key, val in self.riven.items():
            if val < 0:
                numNeg += 1
            elif val > 0:
                numPos += 1
            else:
                continue # Attribute is not on riven
        if numPos == 3 and numNeg == 0:
            return # Values are set to 3p0n by default
        elif numPos == 3 and numNeg == 1:
            posMulti = 1.25 # Negative values are set to 3p1n by default
        elif numPos == 2 and numNeg == 0:
            posMulti = 1.32
        elif numPos == 2 and numNeg == 1:
            posMulti = 1.65
            negMulti = 0.66
        else: # Something is wrong (ie 4 positives or 2 negatives)
            posMulti = 0
            negMulti = 0

        for key, val in self.riven.items():
            if val < 0:
                self.riven[key] = round(val * negMulti,3)
            elif val > 0:
                self.riven[key] = round(val * posMulti,3)
            else:
                continue # Attribute is not on riven
        



        







    
