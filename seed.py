from person import Person
from muscle import Muscle
from musclegroup import MuscleGroup
from exercise import Exercise


# Exercise: (name, targets, time, equipment = None)
# # name = Person instance object
# # targets = list of MuscleGroup instance objects
# # time = integer, in minutes
# # equipment = either a string, or None
#
# Person: (name, nogos)
# # name = string
# # nogos = list of Exercise instance objs that Person hates
#
# Muscle: (name)
#
# MuscleGroup: (name, muscles)
# name = string
# muscles = list of Muscle instance objects

#GETGAINS_BY_MUSCLE_GROUP(me, [abs, arms], 10, False):

def WORKOUT_BY_MUSCLE_GROUP(who, what, how_long, equipment):
    # first filter by equipment
    if equipment == False:
        exercises = Exercise.exercises_without_equipment(Exercise.all)
    else:
        exercises = Exercise.all
    # then filter by person
    exercises = who.acceptable_exercises(exercises)
    # finally, filter by muscle group
    yes = []
    for group in what:
        yes += group.musclegroup_exercises(exercises)
    # start creating workout!!!
    workout = Exercise.populate_workout(how_long, exercises)
    # getting output...
    return Exercise.gimme_gains(workout)



upperabs = Muscle("Upper Abs")
lowerabs = Muscle("Lower Abs")
obliques = Muscle("Obliques")
shoulders = Muscle("Shoulders")
glutes = Muscle("Glutes")
thighs = Muscle("Thighs")
biceps = Muscle("Biceps")
triceps = Muscle("Triceps")
chest = Muscle("Chest")

crunches = Exercise('Crunches x20', [upperabs], 1) #
legraise = Exercise('Leg Raises x15', [lowerabs], 2) #
plank = Exercise('Plank: 90sec', [upperabs, lowerabs, shoulders], 2) #
sideplank = Exercise('Side Planks: 45sec/side', [upperabs, lowerabs, obliques, shoulders], 2) #
bikecrunch = Exercise('Bicycle Crunches x40', [upperabs, obliques], 1) #
jackknives = Exercise('Jackknives x10', [upperabs, lowerabs, obliques], 1) #
squats = Exercise('Regular Squats x20', [glutes, thighs, lowerabs], 1)
kettlebells = Exercise('Kettlebell Swings x30', [glutes], 2, 'Kettlebell')
sumos = Exercise('Sumo Squats x20', [glutes, thighs, lowerabs], 1) #
pushups = Exercise('Push Ups x20', [shoulders, lowerabs, thighs], 1) #
deadlifts = Exercise('Deadlifts x30', [glutes, thighs], 2, 'Barbell')
bicepcurls = Exercise('Bicep Curls x20', [biceps], 1, "Dumbbells")
tricepdips = Exercise('Tricep Dips x20', [triceps, shoulders], 1, 'Bench')
shoulderpress = Exercise('Shoulder Press x20', [shoulders, triceps], 1, 'Dumbbells')
rows = Exercise('Dumbbell Rows x20/side', [triceps, shoulders], 1, 'Dumbbells')
chestpress = Exercise('Chest Press x15', [chest, shoulders], 1, 'Barbell')

abs = MuscleGroup('Abs', [upperabs, lowerabs, obliques])
arms = MuscleGroup('Arms', [biceps, triceps, shoulders])
upperbod = MuscleGroup('Upper Body', [chest, shoulders, biceps, triceps])
lowerbod = MuscleGroup('Lower Body', [glutes, thighs])

me = Person('Me', [squats, sumos])
kimmy = Person('Kimmy', [rows, bicepcurls])
titus = Person('Titus', [crunches, sideplank])
lillian = Person('Lillian', [jackknives, bikecrunch])

# def WORKOUT_BY_SPECIFIC_MUSCLES(who, what, when, equipment):
#
#
