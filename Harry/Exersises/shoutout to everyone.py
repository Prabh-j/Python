import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice") 

names = ['John', 'Taravangian', 'Lewis Therin Talamon','Prabhjot Singh Dhaliwal', 'Odium']

for i in names:
    speaker.speak(f"Shoutout to {i}")





#from os import system #system function excute command in terminal
#system('mkdir nki.txt') 






