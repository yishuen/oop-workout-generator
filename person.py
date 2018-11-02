from exercise import Exercise

class Person:

    def __init__(self, name, nogos):
        self.name = name
        self.nogos = nogos

    def acceptable_exercises(self, exercises):
        return list(filter(lambda n: n not in self.nogos, exercises))
