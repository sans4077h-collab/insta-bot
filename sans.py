from instagrapi import Client
import time
from datetime import datetime

# --- إعدادات الحساب ---
USERNAME = 'sans_7_4'
PASSWORD = 'ksmk12345'  # تأكد أنه باسورده الصحيح
GROUP_ID = '949847180867720'

# --- ✍️ عدل رسالتك هنا ---
MESSAGE_TEXT = "احدهم يجرب"

cl = Client()

def start_bot():
    try:
        print("🚀 Running without proxy for stability...")
        
        print("🚀 Login attempt...")
        cl.login(USERNAME, PASSWORD)
        print("✅ Logged in successfully!")

        while True:
            try:
                # إرسال الرسالة للمجموعة
                cl.direct_send(MESSAGE_TEXT, thread_ids=[GROUP_ID])
                
                now = datetime.now().strftime("%H:%M:%S")
                print(f"✅ Message sent at {now}")
                
                # الانتظار لمدة 20 دقيقة (1200 ثانية)
                print("😴 Waiting for 20 minutes...")
                time.sleep(80)
                
        except Exception as e:
                print(f"❌ Error sending message: {e}")
                time.sleep(60) # انتظر دقيقة وحاول مجدداً

    except Exception as e:
        print(f"❌ Login failed: {e}")

if __name__ == "__main__":
    start_bot()
