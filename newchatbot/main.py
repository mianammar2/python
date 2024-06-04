import webbrowser
import nltk
from nltk.chat.util import Chat, reflections
# Define pairs of patterns and responses
pairs = [
    [r"my name is (.*)", ["Hello %1, How are you today?"]],
    [r"hi|hey|hello", ["Hello!", "Hey there!", "Hi, how can I help you?"]],
    [r"what is your name?", ["I am a Geeky Beasts created by Alpha group. You can call me GB."]],
    [r"how are you?", ["I'm doing good. How about you?", "I'm just a program, but I'm here to help you!"]],
    [r"sorry (.*)", ["It's alright", "No problem", "Don't worry about it"]],
    [r"I am (.*) (good|well|okay|ok)", ["Nice to hear that!", "Alright, great!"]],
    [r"(.*) age?", ["I am a computer program, I don't have an age.", "Age is just a number for me!"]],
    [r"what (.*) want?", ["I want to help you with your questions.", "I am here to assist you."]],
    [r"who (.*) created?", ["I was created by OpenAI.", "Some very smart people at OpenAI made me."]],
    [r"who are you?", ["I am an AI chatbot created by OpenAI.", "I'm ChatGPT, your virtual assistant."]],
    [r"what can you do?", ["I can chat with you, answer questions, and help you with information.", "I'm here to assist you with various queries."]],
    [r"what is (.*)?", ["%1 is something I'm happy to help you with!", "Let's talk more about %1."]],
    [r"where (.*) located?", ["I'm based in the cloud, I don't have a physical location.", "I exist in the digital world."]],
    [r"how is the weather?", ["I can't check the weather right now, but you can check it online!", "Please check a weather website or app for that information."]],
    [r"do you (.*) love?", ["I'm a machine, so I don't have feelings, but I'm here to help you!", "I can't experience love, but I can help you with information about it."]],
    [r"what is your favorite (.*)?", ["I don't have preferences like humans, but I'm happy to talk about %1.", "I can help you find information about %1."]],
    [r"how do you work?", ["I process language and respond based on patterns and algorithms.", "I use machine learning to understand and generate responses."]],
    [r"tell me a joke", ["Why don't scientists trust atoms? Because they make up everything!", "What do you call fake spaghetti? An impasta!"]],
    [r"tell me a fun fact", ["Did you know honey never spoils?", "A day on Venus is longer than a year on Venus."]],
    [r"what is the capital of (.*)?", ["The capital of %1 is something I can look up for you!", "You can find the capital of %1 in a world atlas or online."]],
    [r"how to (.*)?", ["I can help you find instructions on how to %1.", "You can search online for tutorials on how to %1."]],
    [r"why (.*)?", ["That's an interesting question. Why do you think %1?", "There could be many reasons why %1."]],
    [r"open (.*) website", ["Opening %1 website for you.", lambda matches: open_website(matches.group(1))]],
    [r"quit", ["Bye for now. See you soon.", "It was nice talking to you. Goodbye!"]],
]

# Function to open websites
def open_website(site_name):
    url = f"https://{site_name}.com"
    webbrowser.open(url)

# Create a chatbot instance
def chatbot():
    print("Hi, I'm a Geeky Beasts. Type 'quit' to exit.")  # Greeting message
    chat = Chat(pairs, reflections)
    chat.converse()

# Run the chatbot
if __name__ == "__main__":
    chatbot()
