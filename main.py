
from pet import Squirrel
import time

def main():
    """Runs the interactive squirrel pet simulation with expanded features."""
    # Create a squirrel object
    pet_name = input("Enter your squirrel's name: ").strip()
    if not pet_name:
        pet_name = "Nippy"  # Another default name
    my_squirrel = Squirrel(pet_name)
    print(f"\nWelcome {my_squirrel.name} the Squirrel! It's currently {my_squirrel.current_season}.")

    # Main interaction loop
    while True:
        print(f"\n--- What would you like to do with {my_squirrel.name}? ---")
        print("1. Feed (Acorns)")
        print("2. Feed (Special Treat)")
        print("3. Let it Sleep")
        print("4. Play Time")
        print("5. Grooming Session")
        print("6. Go Acorn Hunting")
        print("7. Build a Nest")
        print("8. Teach a New Trick")
        print("9. Practice a Trick")
        print("10. Check Squirrel's Status")
        print("11. One Year Older")
        print("12. Unexpected Event!")
        print("13. Talk to Your Squirrel")
        print("14. Play Nut Hunt!")
        print("15. Change Season")
        print("0. Say Goodbye")

        choice = input("Enter your choice (0-15): ").strip()

        if choice == '1':
            my_squirrel.eat()
        elif choice == '2':
            treat = input(f"What special treat would you like to give to {my_squirrel.name}? ")
            my_squirrel.eat(treat)
        elif choice == '3':
            my_squirrel.sleep()
        elif choice == '4':
            my_squirrel.play()
        elif choice == '5':
            my_squirrel.groom()
        elif choice == '6':
            my_squirrel.collect_acorns()
        elif choice == '7':
            my_squirrel.build_nest()
        elif choice == '8':
            trick = input("Enter a trick for your squirrel to teach: ").strip()
            if trick:
                my_squirrel.train(trick)
            else:
                print("What trick should your squirrel try to learn?")
        elif choice == '9':
            trick_to_practice = input(f"Which trick would you like to practice with {my_squirrel.name}? ").strip()
            if trick_to_practice:
                my_squirrel.practice_trick(trick_to_practice)
            else:
                print("Please enter the name of a trick to practice.")
        elif choice == '10':
            my_squirrel.get_status()
        elif choice == '11':
            my_squirrel.age_squirrel()
        elif choice == '12':
            my_squirrel.random_event()
        elif choice == '13':
            phrase = input("What would you like to say to your squirrel? ").strip()
            my_squirrel.talk(phrase)
        elif choice == '14':
            my_squirrel.play_nut_hunt()
        elif choice == '15':
            new_season = input(f"What season should it be? (Spring, Summer, Autumn, Winter): ").strip().capitalize()
            if new_season in ["Spring", "Summer", "Autumn", "Winter"]:
                my_squirrel.change_season(new_season)
            else:
                print("Invalid season. Please enter Spring, Summer, Autumn, or Winter.")
        elif choice == '0':
            print(f"Goodbye for now! Take wonderful care of {my_squirrel.name}! May your days be filled with sunshine and nuts! 🐿️")
            break
        else:
            print("Invalid choice. Please enter a number between 0 and 15.")

        # Simulate time passing
        time.sleep(1.5)

if __name__ == "__main__":
    main()
