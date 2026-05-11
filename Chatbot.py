# Simple AI Style Chatbot

import random

greetings = ["hi", "hello", "hey", "hii"]
greeting_reply = [
    "Hello! How can I help you today?",
    "Hi! Welcome.",
    "Hey! Nice to meet you."
]

price_words = ["price", "cost", "rate"]
price_reply = [
    "Our products start from Rs. 500.",
    "Prices are affordable.",
    "Different products have different prices."
]

delivery_words = ["delivery", "shipping"]
delivery_reply = [
    "Delivery takes 3 to 5 days.",
    "Fast delivery is available."
]

print("===== AI CUSTOMER CHATBOT =====")

while True:

    user = input("\nYou: ").lower()

    if any(word in user for word in greetings):
        print("Bot:", random.choice(greeting_reply))

    elif any(word in user for word in price_words):
        print("Bot:", random.choice(price_reply))

    elif any(word in user for word in delivery_words):
        print("Bot:", random.choice(delivery_reply))

    elif "bye" in user:
        print("Bot: Goodbye! Have a nice day.")
        break

    else:
        print("Bot: Sorry, I don't understand.")
