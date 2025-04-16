class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []
        self.acorns = 0

    def eat(self):
        self.hunger = max(self.hunger - 3, 0)
        self.happiness = min(self.happiness + 1, 10)
        print(f"{self.name} is munching on crunchy acorns! 🌰🐿️")

    def sleep(self):
        self.energy = min(self.energy + 5, 10)
        print(f"{self.name} curls up in a tree nest and snoozes. 💤")

    def play(self):
        if self.energy < 2:
            print(f"{self.name} is too tired to play... 😴")
            return
        self.energy -= 2
        self.happiness = min(self.happiness + 2, 10)
        self.hunger = min(self.hunger + 1, 10)
        print(f"{self.name} scurries around chasing leaves! 🍂")

    def get_status(self):
        print(f"\n{self.name}'s Current Status:")
        print(f"🌰 Hunger: {self.hunger}")
        print(f"⚡ Energy: {self.energy}")
        print(f"😊 Happiness: {self.happiness}")
        print(f"🎒 Acorns Collected: {self.acorns}")
        print(f"🎩 Tricks: {', '.join(self.tricks) if self.tricks else 'None'}\n")

    def train(self, trick):
        self.tricks.append(trick)
        print(f"{self.name} has learned to {trick}! 🧠")

    def show_tricks(self):
        if self.tricks:
            print(f"{self.name} knows these tricks: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} hasn’t learned any tricks yet.")

    # Bonus Custom Actions
    def groom(self):
        self.happiness = min(self.happiness + 2, 10)
        print(f"{self.name} grooms its fluffy tail. Looking sharp! ✨")

    def collect_acorns(self):
        if self.energy < 1:
            print(f"{self.name} is too tired to collect acorns. 💤")
            return
        self.energy -= 1
        self.happiness = min(self.happiness + 1, 10)
        self.acorns += 1
        print(f"{self.name} found a shiny acorn! 🌰 Total: {self.acorns}")