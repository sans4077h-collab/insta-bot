from instagrapi import Client
import time
from datetime import datetime

# --- إعدادات الحساب (تأكد من كتابتها بين علامات التنصيص) ---
USER = "sans_7_4"
PASS = "ksmk12345"
GROUP_ID = "949847180867720"

# --- ✍️ خانة الرسالة (اكتب اللي تبي هنا) ---
MESSAGE_TEXT = "احدهم يجرب"

cl = Client()

def start_bot():
    try:
        # تنظيف اليوزر من أي مسافات مخفية
        clean_user = USER.strip()
        print(f"📡 Attempting login for: [{clean_user}]")
        
        # محاولة الدخول
        cl.login(clean_user, PASS)
        print("✅ Logged in successfully!")

        while True:
            try:
                cl.direct_send(MESSAGE_TEXT, thread_ids=[GROUP_ID])
                print(f"✅ Message sent at {datetime.now().strftime('%H:%M:%S')}")
                time.sleep(220) # يرسل كل 20 دقيقة
            except Exception as e:
                print(f"❌ Error during sending: {e}")
                time.sleep(60)

    except Exception as e:
        print(f"❌ Login failed! Error: {e}")

if __name__ == "__main__":
    start_bot()
