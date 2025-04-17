from pet import Pet
import time

def main():
    # Create a pet object
    pet_name = input("Enter your pet's name: ")
    pet_type = "Squirrel"  # Fixed to Squirrel
    my_pet = Pet(pet_name, pet_type)
    print(f"Creating pet: {my_pet.name} the {my_pet.pet_type}!")

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
        print("8. Age Pet")
        print("9. Random Event")
        print("0. Exit")

        choice = input("Enter your choice (0-9): ")

        if choice == '1':
            my_pet.eat()
        elif choice == '2':
            my_pet.sleep()
        elif choice == '3':
            my_pet.play()
        elif choice == '4':
            my_pet.groom()
        elif choice == '5':
            my_pet.collect_acorns()
        elif choice == '6':
            trick = input("Enter a trick for your pet to learn: ")
            my_pet.train(trick)
        elif choice == '7':
            my_pet.get_status()
        elif choice == '8':
            my_pet.age_pet()
        elif choice == '9':
            my_pet.random_event()
        elif choice == '0':
            print("Goodbye! Take care of your pet! Remember, acorns are life! 🐿️")
            break
        else:
            print("Invalid choice. Please try again.")

        # Simulate time passing
        time.sleep(1)

if __name__ == "__main__":
    main()