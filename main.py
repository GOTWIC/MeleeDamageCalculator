import pandas as pd

import APIhandler
import Calculator
import Melee
import Settings

# Get list of melee weapons from APIhandler.py
meleeWeapons = APIhandler.getMeleeWeps()

# Create Melee Build using Settings.py
build = Melee.MeleeBuild(Settings.mods, Settings.rivenSettings, Settings.otherSettings)

data = []

for wep in meleeWeapons:
    data.append(Calculator.calculateMeleeDMG(wep, build))

df = pd.DataFrame(data, columns=['Name', 'Slash DPS - No Stance', 'Best Neutral Stance', 'Slash DPS - Neutral', 'Best Forward Stance', 'Slash DPS - Forward'])

df.sort_values(by=['Slash DPS - No Stance'], ascending=False, inplace=True, ignore_index=True)


print(df.head(20))

df.to_csv('results.csv')
