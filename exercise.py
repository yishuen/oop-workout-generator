from muscle import Muscle

class Exercise:

    all = []

    def __init__(self, name, targets, time, equipment = None):
        self.name = name
        self.targets = targets
        self.time = time
        self.equipment = equipment
        Exercise.all.append(self)

    @classmethod
    def exercises_without_equipment(cls, exercises):
        return list(filter(lambda e: e.equipment == None, exercises))

    @classmethod
    def populate_workout(cls, duration, exercises):
        workout = []
        time_elapsed = 0
        from random import choice
        while time_elapsed < duration:
            pick = choice(exercises)
            workout.append(pick)
            time_elapsed += pick.time
        return workout

    @classmethod
    def gimme_gains(cls, workout):
        titles = list(map(lambda ex: ex.name, workout))
        exercises_with_stuff = list(filter(lambda ex: ex.equipment != None, workout))
        stuff = list(map(lambda s: s.equipment, exercises_with_stuff))
        if stuff == []:
            return "Your Workout: " + ', '.join(titles)
        else:
            return "Your Workout: " + ', '.join(titles) + ". || Stuff You'll Need: " + ", ".join(set(stuff))
