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
    def __init__(self, mods, otherSettings):
        self.br = mods['Blood Rush'] * 4.4
        self.ss = mods['Sacrificial Steel'] * 2.2
        self.os = mods['Organ Shatter'] * 0.9
        self.gl1 = mods['Gladiator Might'] * 0.6 # cd
        self.gl2 = mods['Gladiator Might'] * 1.1 # cc
        self.co = mods['Condition Overload'] * 0.8 * otherSettings['Procs']
        self.ppp = mods['Primed Pressure Point'] * 1.65
        self.pf = mods['Primed Fury'] * 0.55
        self.bf = mods['Berserker Fury'] * 0.7
        self.pr = mods['Primed Reach'] * 3
        self.slb = mods['Spring-Loaded Blade'] * 2
        self.ww = mods['Weeping Wounds'] * 4.4
        self.vs = mods['Virulent Scourge'] * 0.6 - otherSettings['Unranked Viral' * 0.45] # Both tox and sc
        self.vf = mods['Vicious Frost'] * 0.6 - otherSettings['Unranked Viral' * 0.45] # Both cold and sc
        self.cm1 = mods['Carnis Mandible'] * 0.9 # slash
        self.cm2 = mods['Carnis Mandible'] * 0.6  # sc
        self.b = mods['Bane'] * 0.55
        self.ars = otherSettings['Arcane Strike'] * 0.6
        self.arf = otherSettings['Arcane Fury'] * 1.8







    
