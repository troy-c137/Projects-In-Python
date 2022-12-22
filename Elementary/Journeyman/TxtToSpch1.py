# This program is a basic text to speech program
# You can download the pyttsx3 library from PyPi using the command "pip install pyttsx3" in the terminal
import pyttsx3
engine = pyttsx3.init() #object creation
engine.setProperty('rate', 170)
#rate = engine.getProperty('rate')
#engine.say('My current speaking rate is ' + str(rate))
t_to_s = ''
print("Type 'exit' to quit the program.")
while t_to_s != 'exit':
    t_to_s = input('What should I say?: ')
    engine.say(t_to_s)
    engine.runAndWait()
