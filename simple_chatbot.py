class SimpleChatbot:
    def __init__(self):
        self.context = {}

    def greet(self):
        return "Hello! I'm your simple chatbot. How can I assist you today?"

    def respond_to_basic_questions(self, user_input):
        if "how are you" in user_input.lower():
            return "I'm just a computer program, but thanks for asking!"
        elif "hello" in user_input.lower() or "hi" in user_input.lower():
             return "Hello! How may I help you?."
        elif "what is your name" in user_input.lower():
            return "I'm called SimpleChatbot."
        elif "what do you do" in user_input.lower():
            return "I'm here to help answer your questions and have a chat with you."
        elif "thank you" in user_input.lower():
            return "You're welcome! If you have more questions, feel free to ask."

    def farewell(self):
        return "Goodbye! If you ever want to chat again, just say hi."

    def handle_user_input(self, user_input):
        if "bye" in user_input.lower() or "goodbye" in user_input.lower():
            return self.farewell()
        elif "what did we talk about last time" in user_input.lower():
            if self.context:
                return f"We previously discussed: {', '.join(self.context.values())}"
            else:
                return "I'm sorry, but I don't have any previous context."
        else:
            response = self.respond_to_basic_questions(user_input)
            if response:
                return response
            else:
                return "I'm sorry, I didn't understand that. Can you please rephrase or ask something else?"

    def ask_user_questions(self):
        for _ in range(3):
            user_response = input("Bot: " + self.handle_user_input(input("You: ")))
            self.context[_] = user_response

if __name__ == "__main__":
    chatbot = SimpleChatbot()
    print(chatbot.greet())
    chatbot.ask_user_questions()