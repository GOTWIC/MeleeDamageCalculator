from audioop import add
import copy
from turtle import st
import Stances

def calculateMeleeDMG(w, b):

    # Calculate riven values
    riven = copy.deepcopy(b.riven)
    for key, val in riven.items():
        riven[key] = round(val * w.dispo,3)

    # Calculate basic stats
    cc = w.cc * (1 + b.br + b.ss + b.gm2 + riven['cc'])
    cd = w.cd * (1 + b.os + b.gm1 + riven['cd'])
    crit_multiplier = 1 + cc * (cd-1)
    atkspd = w.speed * (1 + b.pf + b.bf + riven['as'])
    rng = w.range + b.pr + b.slb + riven['rng']
    sc = w.sc * (1 + b.ww + b.vs + b.vf + b.cm2)
    bane = b.b + riven['bane'] # Include roar 

    # Calculate damage
    dmg = copy.deepcopy(w.dmg)
    for type, val in dmg.items():
        dmg[type] = val * (1 + b.co + b.ppp + riven['dmg']) * (1 + bane)


    # To calculate slash weight
    modded_base_dmg = dmg['Total'] 

    # calculate damage type specific mods here
    # ... NOT IMPLEMENTED


    # Bleed damage and chance to proc per hit
    sp_dmg_tick = 0.35 * modded_base_dmg * (1 + bane) * crit_multiplier
    sp_weight = dmg['Slash'] / dmg['Total']
    sp_per_hit = sc * sp_weight


    # Stanceless
    stanceless_sp_per_sec = sp_per_hit * atkspd
    stanceless_sp_dps = stanceless_sp_per_sec * sp_dmg_tick

    # Stance - Neutral
    type = w.type
    stance_neutral_dmgvals = []
    if type in Stances.stances.keys(): # remove this if statement later when all melee weapon types have been implemented
        for stance in Stances.stances[type]:
            numHits = Stances.stances[type][stance]['Neutral']['Attacks']
            exeTime = Stances.stances[type][stance]['Neutral']['Length']
            avgMulti = Stances.stances[type][stance]['Neutral']['Average Multiplier']
            addedSP = Stances.stances[type][stance]['Neutral']['Slash Procs']

            modded_exeTime = exeTime/atkspd
            modded_avgMulti = avgMulti * atkspd

            hits_per_sec = numHits/modded_exeTime
            added_sp_per_sec = addedSP/modded_exeTime

            weapon_sp_per_sec = sp_per_hit * hits_per_sec
            total_sp_per_sec = weapon_sp_per_sec + added_sp_per_sec
            stance_sp_dps = total_sp_per_sec * sp_dmg_tick * modded_avgMulti

            stance_neutral_dmgvals.append((stance, round(stance_sp_dps,0)))

    stance_forward_dmgvals = []
    if type in Stances.stances.keys(): # remove this if statement later when all melee weapon types have been implemented
        for stance in Stances.stances[type]:
            numHits = Stances.stances[type][stance]['Forward']['Attacks']
            exeTime = Stances.stances[type][stance]['Forward']['Length']
            avgMulti = Stances.stances[type][stance]['Forward']['Average Multiplier']
            addedSP = Stances.stances[type][stance]['Forward']['Slash Procs']

            modded_exeTime = exeTime/atkspd
            modded_avgMulti = avgMulti * atkspd

            hits_per_sec = numHits/modded_exeTime
            added_sp_per_sec = addedSP/modded_exeTime

            weapon_sp_per_sec = sp_per_hit * hits_per_sec
            total_sp_per_sec = weapon_sp_per_sec + added_sp_per_sec
            stance_sp_dps = total_sp_per_sec * sp_dmg_tick * modded_avgMulti

            stance_forward_dmgvals.append((stance, round(stance_sp_dps),0))

    stance_neutral_dmgvals.sort(key = lambda x: x[1], reverse=True)
    stance_forward_dmgvals.sort(key = lambda x: x[1], reverse=True)

    # remove the following when all stances have been implemented
    if len(stance_neutral_dmgvals) == 0:
        stance_neutral_dmgvals.append(('-', 0))
    if len(stance_forward_dmgvals) == 0:
        stance_forward_dmgvals.append(('-', 0))
    
    

    return w.name, round(stanceless_sp_dps,2), stance_neutral_dmgvals[0][0], stance_neutral_dmgvals[0][1], stance_forward_dmgvals[0][0], stance_forward_dmgvals[0][1]