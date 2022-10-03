import copy

def calculateMeleeDMG(w, b):
    cc = w.cc * (1 + b.br + b.ss + b.gl2)
    cd = w.cd * (1 + b.os + b.gl1)
    atkspd = w.speed * (1 + b.pf + b.bf)
    rng = w.range + b.pr + b.slb
    sc = w.sc * (1 + b.ww + b.vs + b.vf + b.cm2)
    bane = b.b # Include roar 

    dmg = copy.deepcopy(w.dmg)

    for type, val in dmg.items():
        dmg[type] = val * (1 + b.co + b.ppp) * (1 + bane)

    # do this before adding damage type mods (ie carnis mandible)
    modded_base_dmg = dmg['Total'] 

    # calculate damage type specific mods here
    # ...

    crit_multiplier = 1 + cc * (cd-1)

    # sp = slash proc
    sp_dmg_tick = 0.35 * modded_base_dmg * (1 + bane)
    sp_weight = dmg['Slash'] / dmg['Total']
    sp_chance = sc * sp_weight
    sp_sec = sp_chance * atkspd
    sp_dps = sp_sec * sp_dmg_tick * crit_multiplier

    #dmgtble = [sp_dps*i for i in range(6)]
    #print(dmgtble)

    #tdmgtbl = [sum(dmgtble[0:i]) for i in range(6)]
    #print(tdmgtbl)

    return w.name, round(sp_dps,2)