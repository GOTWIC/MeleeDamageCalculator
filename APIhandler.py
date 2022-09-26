import requests
import json
import Melee as Melee


def apiDMGtoObjectDMG(dmg):
        dmgOBJ = {
            'Total': 0,
            'Impact': 0, 'Puncture': 0, 'Slash': 0, 
            'Cold': 0, 'Heat': 0, 'Electric': 0, 'Toxin': 0, 
            'Corrosive': 0, 'Viral': 0, 'Radiation': 0, 'Blast': 0, 'Magnetic': 0, 'Gas': 0, 
            'Other': 0
        }
        total = 0
        for type, val in dmg.items():

            total += val

            match type:
                case 'Impact':
                    dmgOBJ['Impact'] = val
                case 'Puncture':
                    dmgOBJ['Puncture'] = val
                case 'Slash':
                    dmgOBJ['Slash'] = val
                case 'Cold':
                    dmgOBJ['Cold'] = val
                case 'Heat':
                    dmgOBJ['Heat'] = val
                case 'Electric':
                    dmgOBJ['Electric'] = val
                case 'Toxin':
                    dmgOBJ['Toxin'] = val
                case 'Corrosive':
                    dmgOBJ['Corrosive'] = val
                case 'Viral':
                    dmgOBJ['Viral'] = val
                case 'Radiation':
                    dmgOBJ['Radiation'] = val
                case 'Blast':
                    dmgOBJ['Blast'] = val
                case 'Magnetic':
                    dmgOBJ['Magnetic'] = val
                case 'Gas':
                    dmgOBJ['Gas'] = val
                case _:
                    dmgOBJ['Other'] += val
        dmgOBJ['Total'] = total
        return dmgOBJ

def getMeleeWeps():

    response_API = requests.get('https://wf.snekw.com/weapons-wiki')

    raw_data = response_API.text
    data = json.loads(raw_data)['data']

    meleeWeapons = []


    for weapon in data:
        weaponData = data[weapon]
        if weaponData['Slot'] == 'Melee':
            try:
                meleeWeapons.append(Melee.MeleeWeapon(
                    weaponData['Name'],
                    weaponData['Class'],
                    apiDMGtoObjectDMG(weaponData['Attacks'][0]['Damage']),
                    weaponData['MeleeRange'],
                    weaponData['Attacks'][0]['FireRate'],
                    weaponData['Attacks'][0]['CritMultiplier'],
                    weaponData['Attacks'][0]['CritChance'],
                    weaponData['Attacks'][0]['StatusChance'],
                    weaponData['Disposition'],
                    weaponData['FollowThrough']
                ))
            except KeyError:
                continue

    return meleeWeapons