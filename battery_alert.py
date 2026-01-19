import psutil
import time
from plyer import notification
import os
from dotenv import load_dotenv 
from google import genai


low_alert_sent = False
mid_alert_sent = False
high_alert_sent = False

# Load environment variables (API Key)
load_dotenv()


def get_ai_message(percent):
    """
    Fetches a witty battery alert using Google's Gemini 2.5 Flash model.
    Uses the modern 'google-genai' SDK for future compatibility.
    """
    try:
        # 1. Initialize the modern Client (Stateless & Thread-safe)
        # We use os.getenv directly here for security  
        client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
        
        # 2. Dynamic Prompt Engineering
        instruction = f"My laptop battery is at {percent}%. Give me a funny 5-word warning."

        # 3. Call the Model using the new 'client.models' service
        # Note: Using 'gemini-2.5-flash' based on latest experimental availability
        response =client.models.generate_content(
            model='gemini-2.5-flash',
            contents= instruction
        )

        return response.text
    
    except Exception as e:
        # Graceful Error Handling:
        # If the API fails (internet down, quota exceeded), return a safe backup.
        # We print the error to the console for debugging, but show the user a clean message.
        print(f"DEBUG: AI Error -{e}")
        return f"Battery is at {percent}% (AI Offline)"


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

