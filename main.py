import APIhandler
import DamageCalculator
import Melee
import Settings

# Get list of melee weapons from APIhandler.py
meleeWeapons = APIhandler.getMeleeWeps()

# Create Melee Build using Settings.py
build = Melee.MeleeBuild(Settings.mods, Settings.otherSettings)

# Calculate Damage
stats = DamageCalculator.calculateMeleeDMG(meleeWeapons, build)

print(stats)