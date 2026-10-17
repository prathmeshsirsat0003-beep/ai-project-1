# Project 1: Rule-Based AI Chatbot
# DecodeLabs - Artificial Intelligence

print("=" * 40)
print("       Welcome to AI Chatbot!")
print("=" * 40)

name = input("Bot: Hello! What is your name? ")

print(f"Bot: Nice to meet you, {name}!")
print("Bot: You can talk to me. Type 'bye' to exit.")

while True:
    user_input = input(f"{name}: ").lower().strip()

    if user_input in ["hello", "hi", "hey"]:
        print("Bot: Hello! How can I help you?")

    elif user_input in ["how are you", "how are you?"]:
        print("Bot: I'm doing great! Thanks for asking.")

    elif user_input in ["what is your name", "your name"]:
        print("Bot: I am a Rule-Based AI Chatbot.")

    elif user_input in ["who created you", "who made you"]:
        print("Bot: I was created as an Artificial Intelligence project.")

    elif user_input in ["what can you do", "help"]:
        print("Bot: I can respond to greetings and simple questions.")

    elif user_input in ["thank you", "thanks"]:
        print("Bot: You're welcome!")

    elif user_input in ["bye", "exit", "quit"]:
        print(f"Bot: Goodbye, {name}! Have a nice day.")
        break

    else:
        print("Bot: Sorry, I don't understand that. Please try something else.")
