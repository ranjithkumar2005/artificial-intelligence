import random

class VacuumCleaner:
    def __init__(self, location, performance=0):
        self.location = location
        self.performance = performance

    def move_left(self):
        self.location[1] = max(0, self.location[1] - 1)

    def move_right(self):
        self.location[1] = min(1, self.location[1] + 1)

    def move_up(self):
        self.location[0] = max(0, self.location[0] - 1)

    def move_down(self):
        self.location[0] = min(1, self.location[0] + 1)

    def clean(self):
        print(f"Cleaning dirt at location {self.location}")
        self.performance += 1

def generate_dirt_location():
    return [random.randint(0, 1), random.randint(0, 1)]

def run_vacuum_cleaner(vacuum):
    dirt_locations = [generate_dirt_location() for _ in range(3)]

    print("Initial dirt locations:")
    print(dirt_locations)

    for dirt_location in dirt_locations:
        while vacuum.location != dirt_location:
            move_towards_dirt(vacuum, dirt_location)

        vacuum.clean()

    print(f"Total performance: {vacuum.performance}")

def move_towards_dirt(vacuum, dirt_location):
    if vacuum.location[0] < dirt_location[0]:
        vacuum.move_down()
    elif vacuum.location[0] > dirt_location[0]:
        vacuum.move_up()
    elif vacuum.location[1] < dirt_location[1]:
        vacuum.move_right()
    elif vacuum.location[1] > dirt_location[1]:
        vacuum.move_left()

if __name__ == "__main__":
    initial_location = [random.randint(0, 1), random.randint(0, 1)]
    vacuum_cleaner = VacuumCleaner(initial_location)
    run_vacuum_cleaner(vacuum_cleaner)
