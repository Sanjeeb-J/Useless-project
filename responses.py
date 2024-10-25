def generate_response(intent):
    if intent == "greeting":
        return "Hello! How can I help you?"
    elif intent == "goodbye":
        return "Goodbye! Have a great day!"
    else:
        return "I'm not sure how to respond to that."
