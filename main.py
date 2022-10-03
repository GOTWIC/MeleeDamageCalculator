import pandas as pd

import APIhandler
import Calculator
import Melee
import Settings

# Get list of melee weapons from APIhandler.py
meleeWeapons = APIhandler.getMeleeWeps()

# Create Melee Build using Settings.py
build = Melee.MeleeBuild(Settings.mods, Settings.otherSettings)

data = []

for wep in meleeWeapons:
    data.append(Calculator.calculateMeleeDMG(wep, build))

df = pd.DataFrame(data, columns=['Name', 'Slash DPS', 'Type'])

df.sort_values(by=['Slash DPS'], ascending=False, inplace=True, ignore_index=True)


print(df.head(20))
