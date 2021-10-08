
#Use pip install gtts before executing the code
from gtts import gTTS
import os

#Enter your text
mytext=input("Enter Your text:")

speech=gTTS(text=mytext,lang='en',slow=False)

#save the audio file
speech.save("myaudio.mp3")

#Execute the file
os.startfile("myaudio.mp3")