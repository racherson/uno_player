import os
if os.path.exists("uno.krf"):
  os.remove("uno.krf")
filenames = ['Cards.krf', 'UpdateGameStatePlanning.krf', 'PlayableCardQueries.krf', 'OpponentsState.krf', 'PlanningOntology.krf', 'GameState.krf', 'StrategyHierarchyPlanning.krf']
with open('allUnoFacts.krf', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
outfile.close()
os.rename("allUnoFacts.krf", "uno.krf")
