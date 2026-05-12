# Simple AI Style Chatbot

import re

responses = {
    r"hi|hello|hey":              "Hello! How can I help you today?",
    r"your name":                 "I am WadiaBot, your virtual assistant!",
    r"how are you":               "I'm doing great! Thanks for asking.",
    r"product|service":           "We offer laptops, phones, and accessories. What are you looking for?",
    r"price|cost|how much":       "Prices vary. Please tell me the product name.",
    r"order|track|delivery":      "Please share your order ID and I'll help you track it.",
    r"return|refund|exchange":    "We have a 30-day return policy. Contact support@wadia.com.",
    r"help|support":              "Sure! Tell me your issue and I'll assist you.",
    r"bye|goodbye|exit|quit":     "Goodbye! Have a great day!",
    r"thanks|thank you":          "You're welcome! Anything else I can help with?",
    r"hours|timing|open":         "We are open Mon-Sat, 9 AM to 6 PM.",
    r"location|address|where":    "We are located at Wadia College, Pune-01.",
    r"discount|offer|deal":       "Check our website for latest offers and discounts!",
    r"payment|pay|upi|card":      "We accept UPI, credit/debit cards, and net banking.",
}

def chatbot_response(user_input):
    user_input = user_input.lower()
    for pattern, reply in responses.items():
        if re.search(pattern, user_input):
            return reply
    return "Sorry, I didn't understand that. Can you rephrase?"

print("\n=== WadiaBot - Customer Support Chatbot ===")
print("WadiaBot: Hello! I'm here to help. Type 'bye' to exit.\n")
while True:
    user = input("You: ").strip()
    if not user:
        continue
    reply = chatbot_response(user)
    print(f"WadiaBot: {reply}\n")
    if re.search(r"bye|goodbye|exit|quit", user.lower()):
        break

A chatbot is a software application that interacts with users automatically using text or voice.
An expert system is an AI program that makes decisions using knowledge and rules similar to a human expert.Knowledge + rules
Rule-based chatbot.Because it replies based on predefined rules and patterns.
re isRegular Expression module It is used for:Pattern matching,Searching text, Finding words/symbols inside strings
r means: Raw StringIt tells Python:Treat backslashes and symbols normally. Mostly used with regular expressions.
.strip() removes extra spaces from beginning and end.
Dictionary stores data in key-value pairs.To store patterns and chatbot replies.
chatgpt is An AI-based chatbot that generates human-like responses using large language models.
