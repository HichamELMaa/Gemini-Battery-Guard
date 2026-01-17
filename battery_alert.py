import psutil
import time
from plyer import notification


low_alert_sent = False
mid_alert_sent = False
high_alert_sent = False

while True:

    # 2. Get the battery status 
    battery = psutil.sensors_battery()
    # --- The Alerts ---
    if battery.percent == 100 and high_alert_sent == False:
        notification.notify(
        title="Battery Reminder",
        message="Your Battery is Fully Charged!",
        timeout=10)
        high_alert_sent = True

    
    if battery.percent == 50 and mid_alert_sent == False:
        notification.notify(
        title="Battery Reminder",
        message="Your Battery is at 50%",
        timeout=10)
        mid_alert_sent = True

    if battery.percent <= 25 and low_alert_sent == False:
        notification.notify(
        title="Battery Alert",
        message="Charge Your PC!",
        timeout=10)
        low_alert_sent = True

    # --- The Resets (The "Memory" Clearers) ---     
    if battery.percent < 100:
        high_alert_sent = False
    
    if battery.percent != 50:
        mid_alert_sent = False
    
    if battery.percent > 25:
        low_alert_sent = False
        
    # --- You are protecting your CPU by waiting 60 seconds. ---
    time.sleep(60) 

