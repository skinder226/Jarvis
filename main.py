import webbrowser
import speech_recognition as sr
import pyttsx3
import os
import re
from Models import search_correct
from Models import chat_bot
from AppOpener import open as open_app
from AppOpener import close
from pywinauto.application import Application
from Models import command_identifier





recognizer = sr.Recognizer()

Method_for_talk = input("What method you chose for talking (Talk/Chat): ")
def recognize_speech():
    if(Method_for_talk == "Talk"):
        text = ""
        try:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source,duration=1)
                print("Listening")
                audio_data = recognizer.listen(source)
                print("converting speech to text")
            text = recognizer.recognize_google(audio_data)
            print("You said: " + text)
        except sr.UnknownValueError as e:
            print("Sorry, I could not understand the audio.", e)
        except sr.RequestError as e:
            print(f"Could not request results; check your internet connection. Error: {e}")
        except Exception as e:
            print(e)

        return text.lower() if text else ""
    else:
        return input("You: ").lower()
    


# Characters that should never be spoken
BLOCKED_CHARS = r"[#\-_.!?|]" \
""

def filter_text(text):
    # Remove blocked characters from the text
    return re.sub(BLOCKED_CHARS, "", text)

def speak(text):
    text = filter_text(text)

    # Don't speak empty text
    if not text.strip():
        return

    engine = pyttsx3.init()
    engine.setProperty('rate', 220)
    engine.setProperty('volume', 1)

    engine.say(text)
    engine.runAndWait()


if __name__ == "__main__": 
    print("Initializing jarvis...")
    speak("Initializing jarvis...")
    while True:
        text = recognize_speech()
        if(text and ("exit" in text or "quit" in text or "stop" in text)):
            print("Exiting jarvis...")
            speak("Exiting jarvis...")
            break
        if(text and "jarvis" in text):
            split_text = text.split("jarvis", 1)
            command_text = split_text[1].strip()
            if command_text:
                identify_command = command_identifier.connect_to_groq(command_text)
                command_response = identify_command.choices[0].message.content.strip()
                print(f"Identified Command: {command_response}")
        
                action, app, task = command_response.split("|", 2)
                action = action.strip().upper()
                app = app.strip().lower()
                task = task.strip().lower()


                
                if action == "OPEN_APP": 
                    try:
                        open_app(app, match_closest=True, output=False)
                        print(f"Opening application {app}")
                    except Exception as e:
                        print("Error:", e)


                elif action == "SEARCH":
                   try:        
                        responce = search_correct.connect_to_groq(command_response)
                        link = responce.choices[0].message.content.strip()
                        webbrowser.open(link)
                        speak(f"Searching for {task}")
                   except Exception as e:
                        print("Error:", e)

                elif action == "OPEN_WEBSITE":
                    webbrowser.open(f"https://{app}.com")
                    speak(f"Opening website {app}")

                elif action == "CLOSE_APP":
                    try:
                        close(app, match_closest=True, output=False)
                        print(f"Closing application {app}")
                    except Exception as e:
                        print("Error:", e)
                        
                elif action == "CHAT":
                    try:
                        response = chat_bot.connect_to_groq(f"{task}")
                        answer = ""
                        print("\n")
                        sentence_buffer = ""

                        for chunk in response:
                            if not chunk:
                                continue

                            print(chunk, end="", flush=True)
                            content = str(chunk)

                            answer += content
                            sentence_buffer += content


                            if any(p in sentence_buffer for p in [".", "!", "?"]):
                                sentence_buffer = ""
                        print("\n")

                        if sentence_buffer.strip():
                            speak(sentence_buffer)
                    except Exception as e:
                        print("Error during chating:", e)

                elif action == "CREATE_FILE":
                    with open(f"{task}", "w", encoding="utf-8") as f:
                        f.write("")

                elif action == "CREATE_FOLDER":
                    os.makedirs(f"{task}", exist_ok=True)

                elif action == "WRITING":
                    app_name, file_name = app.split(":", 1)
                    app_name = app_name.strip()
                    file_name = file_name.strip()
                    try:
                        with open(f"{file_name}.txt", "w", encoding="utf-8") as f:
                            f.write("")
                        app = Application().start(f"{app_name + ".exe".lower()} {file_name}.txt")
                        notepad = app.UntitledNotepad
                        response = chat_bot.connect_to_groq(f"{task}")
                        answer = ""
                        print("\n")
                        sentence_buffer = ""
                        
                        for chunk in response:
                            if not chunk:
                                continue

                            content = str(chunk)
                            notepad.Edit.type_keys(
                                chunk or "",
                                with_spaces=True
                                )  
                            answer += content
                            sentence_buffer += content
                            
                            print(content, end="", flush=True)

                            if any(p in sentence_buffer for p in [".", "!", "?"]):
                                speak(sentence_buffer)
                                sentence_buffer = ""
                        print("\n")
                    except Exception as e:
                        print("Error:", e)
                  
                elif action == "SYSTEM_CONTROL":
                    if "shutdown" in task:
                        os.system("shutdown /s /t 1")
                    elif "restart" in task:
                        os.system("shutdown /r /t 1")
                    elif "sleep" in task:
                        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
                    elif "hibernate" in task:
                        os.system("rundll32.exe powrprof.dll,SetSuspendState Hibernate")
                    speak(f"Performing {task} command")
                    

  