import speech_recognition
import pyttsx3
from datetime import date, datetime
import requests
import openai

openai.api_key = "YOUR_OPENAI_API_KEY"

def chat_with_gpt(user_input):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_input}]
    )
    return response["choices"][0]["message"]["content"]

def get_weather(city):
    api_key = "af69ed298753a2a21992ae5c13236714"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data["cod"] == 200:
        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]
        return f"The temperature in {city} is {temp}°C with {desc}."
    else:
        return "City not found."

robot_ear = speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()
robot_brain =""

while True:

    with speech_recognition.Microphone() as mic:
        print("Robot: I'm Listening")
        audio = robot_ear.listen(mic)

    print("Robot:...")

    try:
        you = robot_ear.recognize_google(audio)
    except:
        you = ""

    print("You: "+you)

    if you =="":
        robot_brain = "I can't hear you, try again"
    elif "hello" in you:
        robot_brain = "Hello Xuan Vu"
    elif "today" in you:
        today = date.today()
        robot_brain = today.strftime("%B %d, %Y")
    elif "time" in you:
        now = datetime.now()
        robot_brain = now.strftime("%H hours %M inutes %S seconds")
    elif "vu" in you:
        robot_brain = "Y is dogs"
    elif "weather" in you:
        city = you.replace("weather", "").strip()
        robot_brain = get_weather(city)
    elif "bye" in you:
        robot_brain = "Good Bye"
        print("Robot: "+robot_brain)
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        break
    else:
        query = you.replace("chat", "").strip()
        robot_brain = chat_with_gpt(query)
    print("Robot: "+robot_brain)
    robot_mouth.say(robot_brain)
    robot_mouth.runAndWait()