import pandas as pd
import copy

import APIhandler
import Calculator
import Melee
import Settings


def CalculateRivens(weaponSample, rivens):

    print('Started Riven Calculations')

    for riven in rivens:
        rivenSettings = copy.deepcopy(Settings.rivenSettings)

        # Reset Settings
        for key in rivenSettings.keys():
            rivenSettings[key] = 0
        # Set the desired stats
        for stat in riven:
            rivenSettings[stat] = 1
        build = Melee.MeleeBuild(Settings.mods, rivenSettings, Settings.otherSettings)

def main():

    print()

    # Get list of melee weapons from APIhandler.py
    meleeWeapons = APIhandler.getMeleeWeps()

    # Create Melee Build using Settings.py
    build = Melee.MeleeBuild(Settings.mods, Settings.rivenSettings, Settings.otherSettings)

    data = []

    # Damage Calculation
    for wep in meleeWeapons:
        data.append(Calculator.calculateMeleeDMG(wep, build))

    # Create Dataframe, send to CSV
    df = pd.DataFrame(data, columns=['Name', 'Slash DPS - No Stance', 'Best Neutral Stance', 'Slash DPS - Neutral', 'Best Forward Stance', 'Slash DPS - Forward'])
    df.to_csv('results.csv', index=False)

    df.sort_values(by='Slash DPS - Forward', ascending=False, inplace=True)



    #Calculate Riven Rating
    weaponSample = ['Dual Ether','Dual Kamas Prime','Kronen Prime','Nami Skyla Prime','Nikana Prime','Orthos Prime','Prisma Dual Cleavers']
    rivens = [
        ['+Critical Damage','+Attack Speed','+Range','-Harmless'],
        ['+Critical Damage','+Attack Speed','-Harmless'],
        ['+Critical Damage','+Attack Speed','+Bane','-Harmless'],
        ['+Critical Damage','+Attack Speed','+Critical Chance','-Harmless'],
        ['+Critical Damage','+Bane','-Harmless'],
        ['+Bane','+Attack Speed','-Harmless'],
    ]


    CalculateRivens(weaponSample,rivens)


    print()
    print('Completed Calculations')
    print()


if __name__ == '__main__':
    main()


