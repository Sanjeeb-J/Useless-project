from chatbot.core import Chatbot

def main():
    chatbot = Chatbot()
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        response = chatbot.get_response(user_input)
        print(f"Bot: {response}")

if __name__ == "__main__":
    main()
