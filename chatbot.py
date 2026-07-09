def chatbot():
    print("=" * 50)
    print("🤖 Welcome to SmartBot!")
    print("Type 'help' to see available commands.")
    print("Type 'bye' to exit.")
    print("=" * 50)

    while True:
        user = input("\nYou: ").lower()

        # Greetings
        if user in ["hi", "hello", "hey"]:
            print("Bot: Hello! Nice to meet you.")

        # How are you
        elif user == "how are you":
            print("Bot: I'm doing great! Thanks for asking.")

        # Name
        elif user == "what is your name":
            print("Bot: My name is SmartBot.")

        # Age
        elif user == "how old are you":
            print("Bot: I was created recently, so I'm very young!")

        # Creator
        elif user == "who created you":
            print("Bot: I was created using Python programming.")

        # Time
        elif user == "time":
            from datetime import datetime
            current_time = datetime.now().strftime("%H:%M:%S")
            print("Bot: Current time is", current_time)

        # Date
        elif user == "date":
            from datetime import datetime
            current_date = datetime.now().strftime("%d-%m-%Y")
            print("Bot: Today's date is", current_date)

        # Joke
        elif user == "tell me a joke":
            print("Bot: Why do programmers prefer dark mode?")
            print("Bot: Because light attracts bugs!")

        # Favorite language
        elif user == "favorite language":
            print("Bot: Python is my favorite language!")

        # Simple math
        elif user == "2+2":
            print("Bot: 4")

        elif user == "5*5":
            print("Bot: 25")

        # Help
        elif user == "help":
            print("\nAvailable Commands:")
            print("- hi")
            print("- hello")
            print("- how are you")
            print("- what is your name")
            print("- how old are you")
            print("- who created you")
            print("- time")
            print("- date")
            print("- tell me a joke")
            print("- favorite language")
            print("- 2+2")
            print("- 5*5")
            print("- bye")

        # Exit
        elif user == "bye":
            print("Bot: Goodbye! Have a nice day.")
            break

        # Unknown input
        else:
            print("Bot: Sorry, I don't understand that command.")

# Run chatbot
chatbot()
