from muscle import Muscle

class MuscleGroup:
    def __init__(self, name, muscles):
        self.name = name
        self.muscles = muscles

    def musclegroup_exercises(self, exercises):
        return list(filter(lambda e: e in self.muscles, exercises))

# abs = MuscleGroup('Abs', [upperabs, lowerabs, obliques])
# arms = MuscleGroup('Arms', [biceps, triceps, shoulders])
# upperbod = MuscleGroup('Upper Body', [chest, shoulders, biceps, triceps])
# lowerbod = MuscleGroup('Lower Body', [glutes, thighs])
