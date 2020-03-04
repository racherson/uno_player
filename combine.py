import os
if os.path.exists("uno.krf"):
  os.remove("uno.krf")
filenames = ['cards.krf', 'strategy.krf', 'opponents.krf']# 'gameState.krf']
with open('allUnoFacts.krf', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
outfile.close()
os.rename("allUnoFacts.krf", "uno.krf")
