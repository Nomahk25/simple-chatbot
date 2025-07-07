def chatbot():
    print("🤖 Hello! I'm ChatSimple. Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if user_input in ["hi", "hello"]:
            print("ChatSimple: Hello! How can I help you today?")
        elif user_input in ["how are you", "how are you doing"]:
            print("ChatSimple: I'm just a bot, but I'm doing great!")
        elif user_input in ["what is your name", "who are you"]:
            print("ChatSimple: I'm ChatSimple, your friendly chatbot.")
        elif user_input in ["bye", "exit", "quit"]:
            print("ChatSimple: Goodbye! Have a great day. 👋")
            break
        else:
            print("ChatSimple: Sorry, I don't understand that. Try asking something else.")

if __name__ == "__main__":
    chatbot()
