import time

def check_study_status():
    while True:
        user_input = input("""Pulse: Are you studying? (yes/no/exit)
You: """)
        
        if user_input.lower() == "exit":
            print("Pulse: Good luck with your studies! Goodbye!")
            break
        elif user_input.lower() == "yes":
            print("Pulse: Great job! Keep it up!")
        elif user_input.lower() == "no":
            print("Pulse: It's normal to get distracted; Get back to studying!")
        else:
            print("Pulse: Please respond with 'yes', 'no', or 'exit'.")

        print("Pulse: I'll check in again in 15 minutes...\n")
        time.sleep(900)

if __name__ == "__main__":
    check_study_status()