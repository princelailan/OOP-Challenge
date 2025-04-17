from pet import Squirrel
import time

def main():
    # Create a squirrel object
    pet_name = input("Enter your squirrel's name: ")
    my_squirrel = Squirrel(pet_name)
    print(f"Creating squirrel: {my_squirrel.name} the Squirrel!")

    # Main interaction loop
    while True:
        print("\nWhat would you like to do?")
        print("1. Eat")
        print("2. Sleep")
        print("3. Play")
        print("4. Groom")
        print("5. Collect Acorns")
        print("6. Train a Trick")
        print("7. Show Status")
        print("8. Age Squirrel")
        print("9. Random Event")
        print("0. Exit")

        choice = input("Enter your choice (0-9): ")

        if choice == '1':
            my_squirrel.eat()
        elif choice == '2':
            my_squirrel.sleep()
        elif choice == '3':
            my_squirrel.play()
        elif choice == '4':
            my_squirrel.groom()
        elif choice == '5':
            my_squirrel.collect_acorns()
        elif choice == '6':
            trick = input("Enter a trick for your squirrel to learn: ")
            my_squirrel.train(trick)
        elif choice == '7':
            my_squirrel.get_status()
        elif choice == '8':
            my_squirrel.age_squirrel()
        elif choice == '9':
            my_squirrel.random_event()
        elif choice == '0':
            print("Goodbye! Take care of your squirrel! Remember, acorns are life! 🐿️")
            break
        else:
            print("Invalid choice. Please try again.")

        # Simulate time passing
        time.sleep(1)

if __name__ == "__main__":
    main()