import random

class Squirrel:
    def __init__(self, name="Chip"):
        self.name = name
        self.hunger = 50
        self.energy = 50
        self.happiness = 50
        self.cleanliness = 50
        self.acorns = 0
        self.nest_quality = 0
        self.tricks = []
        self.age = 0
        self.current_season = "Spring"

    def eat(self, food="acorns"):
        if food.lower() == "acorns":
            self.hunger = min(100, self.hunger + 20)
            print(f"{self.name} munches on acorns and looks satisfied!")
        else:
            self.hunger = min(100, self.hunger + 30)
            self.happiness = min(100, self.happiness + 10)
            print(f"{self.name} enjoys the special treat: {food}!")

    def sleep(self):
        self.energy = min(100, self.energy + 40)
        print(f"{self.name} curls up in the nest and takes a nap.")

    def play(self):
        if self.energy >= 20 and self.happiness < 100:
            self.energy -= 20
            self.happiness = min(100, self.happiness + 30)
            print(f"{self.name} jumps around playfully!")
        else:
            print(f"{self.name} is too tired or already super happy to play.")

    def groom(self):
        self.cleanliness = 100
        print(f"{self.name} grooms their fluffy tail and feels fresh!")

    def collect_acorns(self):
        found = random.randint(1, 5)
        self.acorns += found
        self.happiness = min(100, self.happiness + 5)
        print(f"{self.name} found {found} acorns!")

    def build_nest(self):
        if self.acorns >= 5:
            self.nest_quality += 10
            self.acorns -= 5
            print(f"{self.name} builds a cozier nest. Nest quality is now {self.nest_quality}.")
        else:
            print(f"{self.name} doesn't have enough acorns to build a nest.")

    def train(self, trick):
        if trick in self.tricks:
            print(f"{self.name} already knows how to {trick}.")
        else:
            self.tricks.append(trick)
            print(f"{self.name} learned how to {trick}!")

    def practice_trick(self, trick):
        if trick in self.tricks:
            print(f"{self.name} performs the trick: {trick}!")
            self.happiness = min(100, self.happiness + 5)
        else:
            print(f"{self.name} doesn't know that trick yet.")

    def get_status(self):
        print(f"""
        --- {self.name}'s Status ---
        Hunger: {self.hunger}/100
        Energy: {self.energy}/100
        Happiness: {self.happiness}/100
        Cleanliness: {self.cleanliness}/100
        Acorns: {self.acorns}
        Nest Quality: {self.nest_quality}/100
        Tricks: {', '.join(self.tricks) if self.tricks else 'None'}
        Age: {self.age} year(s)
        Season: {self.current_season}
        ----------------------------
        """)

    def age_squirrel(self):
        self.age += 1
        self.hunger = max(0, self.hunger - 10)
        self.energy = max(0, self.energy - 10)
        self.cleanliness = max(0, self.cleanliness - 10)
        print(f"{self.name} is now {self.age} year(s) old!")

    def random_event(self):
        event = random.choice([
            "found a shiny nut!",
            "escaped a hawk!",
            "met a friendly rabbit!",
            "learned a new squirrel dance!"
        ])
        self.happiness = min(100, self.happiness + 10)
        print(f"Random event: {self.name} {event}")

    def talk(self, phrase):
        print(f"{self.name} tilts its head and responds: '{phrase}'")

    def play_nut_hunt(self):
        print(f"Welcome to Nut Hunt!")
        found = random.randint(0, 10)
        self.acorns += found
        self.happiness = min(100, self.happiness + found)
        print(f"{self.name} found {found} hidden nuts during the hunt!")

    def change_season(self, season):
        self.current_season = season
        print(f"The season has changed to {season}!")
