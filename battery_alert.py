import psutil
import time
from plyer import notification
import google.generativeai as genai
import os
from dotenv import load_dotenv 



low_alert_sent = False
mid_alert_sent = False
high_alert_sent = False

# 1. Load secrets immediately
load_dotenv()


def get_ai_message(percent):
    #try:

        # 1. Setup the key globally (No variable needed here)
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

        # 2. Define the Model (The "Brain")
        model = genai.GenerativeModel("gemini-2.5-flash")

        # 2.Create the instruction using an f-string
        # Use the 'percent' variable here!
        instruction = f"My laptop battery is at {percent}%. Give me a funny 5-word warning."

        #3. Ask the AI
        response = model.generate_content(instruction)

        #4. Return the text result
        return response.text 
     
   # except:
        # Return the backup message if the AI fails
       # return f"Battery is at {percent}% (AI Offline)"


while True:

    # 1. Get the battery status 
    battery = psutil.sensors_battery()
    # --- The Alerts ---
    if battery.percent >=100 and high_alert_sent == False:

        # ONLY call the AI when the condition is met
        ai_joke = get_ai_message(battery.percent)

        notification.notify(
            title="Battery Reminder",
            message=ai_joke,
            timeout=10
        )
        high_alert_sent = True

    
    if battery.percent == 50 and mid_alert_sent == False:
        # ONLY call the AI when the condition is met
        ai_joke = get_ai_message(battery.percent)

        notification.notify(
            title="Battery Reminder",
            message=ai_joke,
            timeout=10
        )
        mid_alert_sent = True

    if battery.percent <= 25 and low_alert_sent == False:

        # ONLY call the AI when the condition is met
        ai_joke = get_ai_message(battery.percent)

        notification.notify(
            title="Battery Reminder",
            message=ai_joke,
            timeout=10
        )
        low_alert_sent = True

    # --- The Resets (The "Memory" Clearers) ---     
    if battery.percent <= 90:
        high_alert_sent = False
    
    if battery.percent >= 60:
        mid_alert_sent = False
    
    if battery.percent >= 30:
        low_alert_sent = False
        
    # --- You are protecting your CPU by waiting 60 seconds. ---
    time.sleep(60) 

