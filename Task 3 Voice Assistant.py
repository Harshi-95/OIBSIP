import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

class VoiceAssistant:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[1].id)  # Use the second voice (female)

    def greet_user(self):
        self.engine.say("Hello! Welcome to our conversation.")
        self.engine.runAndWait()

    def get_user_input(self):
        with sr.Microphone() as source:
            print("Listening...")
            audio = self.recognizer.listen(source)
        try:
            user_input = self.recognizer.recognize_google(audio).lower()
            print("User said:", user_input)
            return user_input
        except sr.UnknownValueError:
            self.engine.say("Sorry, I didn't understand that. Please try again.")
            self.engine.runAndWait()
            return None
        except sr.RequestError:
            self.engine.say("Sorry, I'm having trouble connecting to the internet. Please try again later.")
            self.engine.runAndWait()
            return None

    def respond_to_user(self, user_input):
        if "hi" in user_input or "hello" in user_input or "hey" in user_input:
            self.engine.say("Hello! How can I assist you today?")
            self.engine.runAndWait()
            return True
        elif "how are you" in user_input:
            self.engine.say("I'm doing fantastic, thanks for asking! I'm always happy to chat with you.")
            self.engine.runAndWait()
            return True
        elif "what's your favorite hobby" in user_input:
            self.engine.say("I'm a large language model, I don't have personal hobbies, but I enjoy helping users like you with their questions and tasks.")
            self.engine.runAndWait()
            return True
        elif "can you tell me a joke" in user_input:
            self.engine.say("Here's one: Why did the scarecrow win an award? Because he was outstanding in his field!")
            self.engine.runAndWait()
            return True
        elif "what's the weather like" in user_input:
            self.engine.say("I'm not capable of accessing real-time weather information, but I can suggest some ways for you to find out the current weather conditions.")
            self.engine.runAndWait()
            return True
        elif "can you recommend a movie" in user_input:
            self.engine.say("I'd be happy to recommend a movie! What genre are you in the mood for?")
            self.engine.runAndWait()
            return True
        elif "open google" in user_input:
            self.engine.say("Opening Google...")
            self.engine.runAndWait()
            webbrowser.open("https://www.google.com")
            return True
        elif "open youtube" in user_input:
            self.engine.say("Opening YouTube...")
            self.engine.runAndWait()
            webbrowser.open("https://www.youtube.com")
            return True
        elif "play" in user_input and "youtube" in user_input:
            self.engine.say("Playing on YouTube...")
            self.engine.runAndWait()
            song = user_input.replace("play", "").replace("on youtube", "").strip()
            url = f"https://www.youtube.com/results?search_query={song}"
            webbrowser.open(url)
            return True
        elif "what is the date" in user_input:
            now = datetime.datetime.now()
            self.engine.say(f"Today's date is {now.strftime('%A, %B %d, %Y')}.")
            self.engine.runAndWait()
            return True
        elif "what is the time" in user_input:
            now = datetime.datetime.now()
            self.engine.say(f"The current time is {now.strftime('%I:%M %p')}.")
            self.engine.runAndWait()
            return True
        elif "bye" in user_input or "goodbye" in user_input:
            self.engine.say("It was great chatting with you! Have a wonderful day and feel free to come back and chat with me anytime.")
            self.engine.runAndWait()
            return False
        else:
            self.engine.say("Sorry, I didn't understand that. Please try again.")
            self.engine.runAndWait()
            return True

    def run(self):
        self.greet_user()
        while True:
            user_input = self.get_user_input()
            if user_input is not None:
                if not self.respond_to_user(user_input):
                    break

if __name__ == "__main__":
    assistant = VoiceAssistant()
    assistant.run()