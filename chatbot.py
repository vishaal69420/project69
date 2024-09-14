Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import nltk
... from nltk.chat.util import Chat, reflections
... 
... # Define pairs of patterns and responses
... pairs = [
...     [
...         r"my name is (.*)",
...         ["Hello %1, how are you today?",]
...     ],
...     [
...         r"what is your name?",
...         ["My name is ChatBot and I'm a chatbot.",]
...     ],
...     [
...         r"how are you?",
...         ["I'm doing well, thank you!", "I'm doing great, thanks for asking.",]
...     ],
...     [
...         r"sorry (.*)",
...         ["Apologies, it's alright.", "No worries.",]
...     ],
...     [
...         r"(.*) thank you (.*)",
...         ["You're welcome!", "No problem.",]
...     ],
...     [
...         r"quit",
...         ["Bye! Take care.", "Goodbye, have a nice day!"]
...     ],
... ]
... 
... # Create a chatbot with defined patterns and responses
... def chatbot():
...     print("Hi, I'm ChatBot! How can I help you today?")
...     chat = Chat(pairs, reflections)
...     chat.converse()
... 
... if __name__ == "__main__":
...     nltk.download('punkt')
...     chatbot()
