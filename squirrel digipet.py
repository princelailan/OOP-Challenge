
import random

class Squirrel:
    """Represents a virtual squirrel pet with various interactions and attributes."""
    def __init__(self, name):
        """Initializes a new Squirrel object."""
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.health = 10
        self.age = 0
        self.tricks = []
        self.acorns_collected = 0
        self.favorite_food = random.choice(["berries", "nuts", "seeds", "mushrooms"])
        self.has_nest = False
        self.found_items = []
        self.current_season = "Autumn"  # Starting season
        print(f"Welcome {self.name}! Did you know {self.name}'s favorite food is {self.favorite_food}? It's currently {self.current_season}.")

    def _change_stat(self, stat_name, change_amount, lower_bound=0, upper_bound=10):
        """Internal helper to change a stat within bounds and print messages."""
        current_value = getattr(self, stat_name)
        new_value = max(lower_bound, min(current_value + change_amount, upper_bound))
        setattr(self, stat_name, new_value)
        return current_value != new_value

    def _check_season_effect(self, activity):
        """Applies minor seasonal effects to energy levels."""
        energy_modifier = 0
        if self.current_season == "Winter":
            if activity in ["play", "collect_acorns", "build_nest"]:
                energy_modifier -= 1
                print(f"The winter chill makes {self.name}'s {activity} a bit more tiring.")
        elif self.current_season == "Summer":
            if activity in ["play", "collect_acorns"]:
                energy_modifier -= 0.5  # Slightly more tiring in summer
                print(f"The summer heat makes {self.name}'s {activity} a little draining.")
        return energy_modifier

    def change_season(self, new_season):
        """Changes the current season."""
        if new_season != self.current_season:
            print(f"The season changes to {new_season}!")
            self.current_season = new_season
        else:
            print(f"It's already {self.current_season}.")

    def eat(self, food="acorns"):
        """Feeds the squirrel, increasing energy and happiness, decreasing hunger."""
        if self.hunger == 0:
            print(f"{self.name} nibbles at the {food} politely. 'Feeling quite full!'")
            return

        if food.lower() == self.favorite_food:
            hunger_reduction = 4
            happiness_increase = 2
            food_message = f"some delightful {self.favorite_food}! '{self.favorite_food}! My absolute favorite treat!'"
        else:
            hunger_reduction = 3
            happiness_increase = 1
            food_message = f"some {food}. 'Yum!'"

        if self._change_stat('hunger', -hunger_reduction):
            self._change_stat('happiness', happiness_increase)
            print(f"{self.name} happily munches on {food_message} 😋")
        else:
            print(f"{self.name} takes a small bite of the {food} but isn't very hungry.")

    def sleep(self):
        """Allows the squirrel to sleep, increasing energy, with a bonus if it has a nest."""
        energy_gain = 4
        message = f"{self.name} curls up and dozes off..."
        if self.has_nest:
            energy_gain = 6
            message = f"{self.name} snuggles into its cozy nest and sleeps soundly..."
            self._change_stat('happiness', 1) # Small happiness boost from a comfy nest
        if self._change_stat('energy', energy_gain):
            print(f"{message} 'Dreaming of tall trees and tasty nuts!' 😴")
        else:
            print(f"{self.name} is restless and can't seem to fall into a deep sleep.")

    def play(self):
        """Allows the squirrel to play, decreasing energy and increasing happiness and hunger."""
        if self.energy < 2:
            print(f"{self.name} twitches its nose wearily. 'Need a little rest first.' 😪")
            return
        energy_cost = 2 + (self._check_season_effect("play") or 0)
        if self._change_stat('energy', -energy_cost):
            self._change_stat('happiness', 2)
            self._change_stat('hunger', 1)
            print(f"{self.name} dashes around, leaping and twirling with joy! 'This is the best!' 😄")
        else:
            print(f"{self.name} tried to play but quickly felt its energy drain.")

    def groom(self):
        """Allows the squirrel to groom itself, increasing happiness."""
        if self._change_stat('happiness', 2):
            print(f"{self.name} meticulously grooms its fur, ensuring every hair is in place. 'Looking quite refined!' ✨")
        else:
            print(f"{self.name}'s fur is already looking impeccably groomed!")

    def collect_acorns(self):
        """Allows the squirrel to collect acorns, decreasing energy and increasing the acorn count and happiness."""
        if self.energy < 1:
            print(f"{self.name} sighs softly. 'So many acorns... so little strength...' 😩")
            return
        energy_cost = 1 + (self._check_season_effect("collect_acorns") or 0)
        if self._change_stat('energy', -energy_cost):
            self._change_stat('happiness', 1)
            self.acorns_collected += 1
            found_something = random.randint(1, 15) # Increased chance of finding something
            if found_something <= 2:
                treasure = random.choice(["a shiny pebble", "a colorful feather", "a smooth acorn shell"])
                self.found_items.append(treasure)
                self._change_stat('happiness', 2)
                print(f"{self.name} unearthed an acorn and... {treasure}! What a delightful surprise! 😄 Total acorns: {self.acorns_collected}, Items: {', '.join(self.found_items)}")
            elif found_something <= 5:
                self._encounter_animal()
            else:
                print(f"{self.name} carefully hides another acorn for future snacking. 'A squirrel's gotta plan!' 🌰 Total acorns: {self.acorns_collected}")
        else:
            print(f"{self.name} was too tired to forage for acorns.")

    def build_nest(self):
        """Allows the squirrel to spend energy building a nest."""
        if self.energy < 3:
            print(f"{self.name} glances around longingly. 'A cozy nest would be nice, but I'm too tired.' 😞")
            return
        energy_cost = 3 + (self._check_season_effect("build_nest") or 0)
        if not self.has_nest and self._change_stat('energy', -energy_cost):
            self.has_nest = True
            self._change_stat('happiness', 2)
            print(f"{self.name} diligently worked and constructed a wonderful nest! 'Home sweet home!' 🏡")
        elif self.has_nest:
            print(f"{self.name} is quite content with its current nest.")
        else:
            print(f"{self.name} attempted to build a nest but lacked the energy to finish.")

    def _encounter_animal(self):
        """Handles random encounters with other animals."""
        animal = random.choice(["a friendly robin", "a sneaky weasel", "a playful bunny", "a wise old owl"])
        print(f"\n{self.name} has an encounter with {animal}!")
        if animal == "a friendly robin":
            self._change_stat('happiness', 1)
            print(f"The robin sang a cheerful tune! {self.name} feels a little brighter. 😊")
        elif animal == "a sneaky weasel":
            self._change_stat('health', -1)
            self._change_stat('happiness', -2)
            print(f"The weasel tried to cause trouble! {self.name} got scared and lost some health and happiness! 😨")
            if self.health <= 0:
                print(f"Oh no! The encounter with the weasel was too dangerous for {self.name}'s well-being!")
        elif animal == "a playful bunny":
            self._change_stat('happiness', 2)
            self._change_stat('energy', -1)
            print(f"{self.name} had a fun chase with the bunny! A bit tiring, but lots of fun! 😄")
        elif animal == "a wise old owl":
            print(f"The owl hooted softly. It seemed to share some ancient wisdom with {self.name}.")
            self._change_stat('happiness', 1) # A moment of connection

    def get_status(self):
        """Prints the current status of the squirrel."""
        print(f"\n--- {self.name}'s Current Status ---")
        print(f"Type: Squirrel")
        print(f"Hunger: {self.hunger}/10")
        print(f"Energy: {self.energy}/10")
        print(f"Happiness: {self.happiness}/10")
        print(f"Health: {self.health}/10")
        print(f"Age: {self.age} years")
        print(f"Favorite Food: {self.favorite_food}")
        print(f"Has Nest: {'Yes' if self.has_nest else 'No'}")
        print(f"Tricks Learned: {', '.join(self.tricks) if self.tricks else 'None yet'}")
        print(f"Acorns Collected: {self.acorns_collected}")
        print(f"Found Items: {', '.join(self.found_items) if self.found_items else 'None'}")
        print(f"Current Season: {self.current_season}")
        print("------------------------------------")

    def train(self, trick):
        """Teaches the squirrel a new trick."""
        if trick.lower() in [t.lower() for t in self.tricks]:
            print(f"{self.name} already knows '{trick}'. Perhaps something more challenging?")
            return
        self.tricks.append(trick)
        print(f"{self.name} put in the effort and learned '{trick}'! 'Watch this!' 🤸")

    def practice_trick(self, trick_name):
        """Allows the user to practice a trick with the squirrel, increasing learning chance."""
        if trick_name.lower() in [t.lower() for t in self.tricks]:
            print(f"{self.name} flawlessly performs '{trick_name}'! Practice makes perfect!")
            self._change_stat('happiness', 1)
            return
        print(f"You and {self.name} work on '{trick_name}' together...")
        if random.randint(1, 3) == 1: # 1 in 3 chance of learning during practice
            self.tricks.append(trick_name)
            self._change_stat('happiness', 2)
            print(f"Amazing! {self.name} mastered '{trick_name}' through practice! 🎉")
        else:
            self._change_stat('energy', -1)
            print(f"{self.name} is still getting the hang of '{trick_name}'. Keep up the practice!")
            if self.energy < 1:
                print(f"{self.name} is too tuckered out to practice anymore.")

    def show_tricks(self):
        """Displays the tricks the squirrel knows."""
        if self.tricks:
            print(f"{self.name} proudly shows off its amazing tricks: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} is still waiting to learn some cool tricks!")

    def age_squirrel(self):
        """Increases the squirrel's age and potentially decreases health as it gets older."""
        self.age += 1
        print(f"{self.name} celebrates another year! It's now {self.age} years young and full of wisdom.")
        if self.age > 10:
            health_loss = random.randint(1, 3)
            self._change_stat('health', -health_loss)
            print(f"{self.name}'s getting a bit old now. Health decreased by {health_loss} to {self.health}.")
            if self.health <= 0:
                print(f"Oh dear! {self.name} has lived a long and cherished life, but is now very frail. Provide extra comfort!")
        elif self.age > 5:
            print(f"{self.name} is in its prime squirrel years.")

    def random_event(self):
        """Triggers a random event that can affect the squirrel's stats or introduce new elements."""
        event = random.choice([
            "discovered a hidden grove of extra tasty nuts!",
            "got momentarily tangled in some vines!",
