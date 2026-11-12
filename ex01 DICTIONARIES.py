contacts = {}

while True:
    print("\nPHONE BOOK")
    print("1. Add contact")
    print("2. Find phone number")
    print("3. Change phone number")
    print("0. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter the person's name: ")
        phone = input("Enter the phone number: ")

        contacts[name] = phone
        print("Contact added successfully!")

    elif choice == "2":
        name = input("Enter the person's name: ")

        if name in contacts:
            print("Phone number:", contacts[name])
        else:
            print("Contact not found!")

    elif choice == "3":
        name = input("Enter the person's name: ")

        if name in contacts:
            phone = input("Enter the new phone number: ")
            contacts[name] = phone
            print("Phone number changed successfully!")
        else:
            print("Contact not found!")

    elif choice == "0":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please try again.")