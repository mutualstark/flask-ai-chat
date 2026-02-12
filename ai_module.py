# ai_module.py

import random

class SimpleAI:
    def __init__(self):
        self.greetings = ["Hello!", "Hi there!", "Hey!", "Greetings!"]

    def generate_response(self, user_input: str) -> str:
        """
        Placeholder AI function.
        This can be replaced later with a real ML model.
        """

        user_input = user_input.lower()

        if "hello" in user_input:
            return random.choice(self.greetings)

        elif "how are you" in user_input:
            return "I'm just a simple AI module, but I'm running perfectly!"

        elif "your name" in user_input:
            return "I am a modular AI powered by Flask."

        elif "bye" in user_input:
            return "Goodbye! Have a great day!"

        else:
            return f"You said: '{user_input}'. This is a placeholder AI response."
