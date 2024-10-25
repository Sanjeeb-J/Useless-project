import re
from .intents import get_intent
from .responses import generate_response
from ..utils.preprocessor import preprocess_text

class Chatbot:
    def __init__(self):
        # Initialization, loading model or intents
        pass
    
    def get_response(self, text):
        processed_text = preprocess_text(text)
        intent = get_intent(processed_text)
        response = generate_response(intent)
        return response
