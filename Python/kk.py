while True:
    # Accept user input
    user_input = input("Enter a command: ")
    # Process user input
    if user_input == "exit":
        # Exit the program
        break
    elif user_input == "help":
        # Display list of available commands
        print("Available commands: exit, help, list, add")
    elif user_input == "list":
        # Display a list of items
        display_items()
    elif user_input == "add":
        # Accept input for the new item
        new_item = input("Enter a new item: ")
        # Add a new item to list
        add_item(new_item)
    else:
        # Invalid command
        print("Invalid command. Enter 'help' for a list of available commands.")
