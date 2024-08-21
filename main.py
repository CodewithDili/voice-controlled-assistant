from voice_recognition import recognize_speech
from nlp_processing import process_command
from tts import speak
from task_automation import automate_task

def main():
    while True:
        print("Listening...")
        command = recognize_speech()
        if command:
            print(f"Command received: {command}")
            response = process_command(command)
            if response:
                speak(response)
                automate_task(response)

if __name__ == "__main__":
    main()
def automate_task(response):
    if "weather" in response:
        # Add your weather fetching code here
        pass
    elif "news" in response:
        # Add your news fetching code here
        pass
    elif "email" in response:
        # Add your email sending code here
        pass
