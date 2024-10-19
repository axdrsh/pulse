import time
import threading
import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    ['my name is (.*)', ['Hello! %1']],
    ['(hi|hello|hey|holla|hola)', ['Hey there!', 'Hi!', 'Hello!']],
    ['(.*) your name ?', ['I am Pulse, a chatbot created using Python and NLTK.']],
    ['(.*) are you ?', ['I am Pulse, a chatbot created using Python and NLTK.']],
    ['(.*) do you do ?', ['I check on you every 20 mins to see if you are studying or not.']],
    ['(.*) created you ?', ['I was created by Adarsh']],
    ['(.*) made you ?', ['I was created by Adarsh']],
    ['(.*) focused', ['Good job! Now go back.']],
    ['Yes', ['Good job! I am proud of you! Now get back to studying.']],
    ['(.*) studied', ['Great! I am proud of you!']],
    ['(.*) did', ['I see. Get back to studying!']],
    ["(.*) distracted", ["Distraction is normal. Get back to studying"]],
    ["No", ["It's okay. Get back to studying"]],
    ["(ok|okay|okayy|k|oka)", ["Yes. Remember every minute counts!"]],
]

chatbot = Chat(pairs, reflections)

def print_study_check():
    while True:
        print("\nPulse: Are you studying?")
        time.sleep(1200)

def start_chat():
    while True:
        user_input = input("-> ")
        response = chatbot.respond(user_input)
        print("Pulse:", response)

if __name__ == "__main__":
    study_check_thread = threading.Thread(target=print_study_check)
    study_check_thread.daemon = True
    study_check_thread.start()
    
    start_chat()
