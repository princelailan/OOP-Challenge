import random

class Squirrel:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.health = 10
        self.age = 0
        self.tricks = []
        self.acorns_collected = 0

    def eat(self):
        if self.hunger == 0:
            print(f"{self.name} looks at you with big, sad eyes. 'I'm already full, human! No more snacks!' 🍽️")
            return
        self.hunger = max(self.hunger - 3, 0)
        self.happiness = min(self.happiness + 1, 10)
        print(f"{self.name} is munching on delicious acorns! 'Yum, crunchy goodness! I could eat these all day!' 🌰")

    def sleep(self):
        self.energy = min(self.energy + 5, 10)
        print(f"{self.name} curls up in a cozy spot... 'Zzz... Dreaming of endless acorns and flying squirrels!' 😴")

    def play(self):
        if self.energy < 2:
            print(f"{self.name} yawns and stretches. 'I’m too tired to play... Maybe after my nap?' 😴")
            return
        self.energy -= 2
        self.happiness = min(self.happiness + 2, 10)
        self.hunger = min(self.hunger + 1, 10)
        print(f"{self.name} is playing happily! 'Catch me if you can! Just kidding, you can't!' 🎉")

    def groom(self):
        self.happiness = min(self.happiness + 2, 10)
        print(f"{self.name} is grooming itself and looks fabulous! 'Check out my fluffy tail! I should be a model!' ✨")

    def collect_acorns(self):
        if self.energy < 1:
            print(f"{self.name} is too tired to collect acorns. 'I need a nap first! Acorns can wait!' 💤")
            return
        self.energy -= 1
        self.happiness = min(self.happiness + 1, 10)
        self.acorns_collected += 1
        print(f"{self.name} found a shiny acorn! 'Score! Total acorns: {self.acorns_collected}. I'm rich!' 🌰")

    def get_status(self):
        print(f"\n{self.name}'s current status:")
        print(f"Type: Squirrel")
        print(f"Hunger: {self.hunger}")
        print(f"Energy: {self.energy}")
        print(f"Happiness: {self.happiness}")
        print(f"Health: {self.health}")
        print(f"Age: {self.age}")
        print(f"Tricks: {', '.join(self.tricks) if self.tricks else 'None'}")
        print(f"Acorns Collected: {self.acorns_collected}")

    def train(self, trick):
        self.tricks.append(trick)
        print(f"{self.name} has learned to {trick}! 'I’m a superstar! Watch me shine!' 🧠")

    def show_tricks(self):
        if self.tricks:
            print(f"{self.name} knows these tricks: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} hasn’t learned any tricks yet. 'Teach me, human! I'm a fast learner!'")

    def age_squirrel(self):
        self.age += 1
        if self.age > 10:
            self.health = max(self.health - 1, 0)
            print(f"{self.name} is getting older... 'I’m wise, not old! Just look at my acorn stash!' Health is now {self.health}.")
        else:
            print(f"{self.name} is now {self.age} years old! 'Still young and spry! Just like a squirrel should be!'")

    def random_event(self):
        event = random.choice([
            "found a toy",
            "got scared by a loud noise",
            "made a new friend",
            "saw a cat and ran away",
            "discovered a hidden stash of acorns"
        ])
        if event == "found a toy":
            self.happiness = min(self.happiness + 3, 10)
            print(f"{self.name} found a new toy!