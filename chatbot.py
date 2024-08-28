def chatbot_response(user_input):
    user_input = user_input.lower()
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you today?"
    elif "how are you" in user_input:
        return "I'm just a bot, but I'm doing great! How about you?"
    elif "what is your name" in user_input:
        return "I am a chatbot . How can I help you?"
    elif "bye" in user_input:
        return "Goodbye! Have a great day!"
    elif "thank you" in user_input or "thanks" in user_input:
        return "You're welcome! If you have any other questions, feel free to ask."
    else:
        return "Sorry, I didn't understand that. Can you please rephrase?"
def chat():
    print("Chatbot: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")
        if "bye" in user_input.lower():
            break
chat()
