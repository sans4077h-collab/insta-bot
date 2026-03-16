from instagrapi import Client
import time
from datetime import datetime

# --- إعدادات الحساب ---
USERNAME = 'sans_7_4'
PASSWORD = 'ksmk12345' 
GROUP_ID = '949847180867720'

# --- ✍️ اكتب رسالتك هنا بين علامات التنصيص ---
MESSAGE_TEXT = "يا هلا! هذه رسالة تلقائية من البوت الخاص بي 🤖"

cl = Client()

def start_bot():
    try:
        print("🚀 Starting bot without proxy...")
        print("🚀 Login attempt...")
        cl.login(USERNAME, PASSWORD)
        print("✅ Logged in successfully!")

        while True:
            try:
                # إرسال الرسالة
                cl.direct_send(MESSAGE_TEXT, thread_ids=[GROUP_ID])
                now = datetime.now().strftime("%H:%M:%S")
                print(f"✅ Message sent at {now}")
                
                # الانتظار 20 دقيقة
                print("😴 Waiting for 20 minutes...")
                time.sleep(80)
            except Exception as e:
                print(f"❌ Error sending message: {e}")
                time.sleep(60)
    except Exception as e:
        print(f"❌ Login failed: {e}")

if __name__ == "__main__":
    start_bot()
