from instagrapi import Client
import time
import os

# --- الإعدادات ---
# الأفضل تحط اليوزر والباسورد هنا مؤقتاً أو تستخدم Environment Variables
USERNAME = 'sans_7_4'
PASSWORD = 'ksmk12345'
GROUP_ID = '949847180867720'
PROXY = 'http://108.165.174.99:3128' # البروكسي الأمريكي اللي اخترناه

cl = Client()

def start_bot():
    try:
        # ضبط البروكسي
        cl.set_proxy(PROXY)
        print(f"📡 Proxy Set: {PROXY}")
        
        print("🚀 Login attempt...")
        cl.login(USERNAME, PASSWORD)
        print("✅ Logged in successfully!")
        
        while True:
            cl.direct_send("🤖 رسالة تلقائية من السيرفر", thread_ids=[GROUP_ID])
            print(f"✅ Message sent at {time.strftime('%H:%M:%S')}")
            # ننتظر 20 دقيقة (1200 ثانية)
            time.sleep(1200)
            
    except Exception as e:
        print(f"❌ Error: {e}")
        print("Retrying in 60 seconds...")
        time.sleep(60)
        start_bot()

if __name__ == "__main__":
    start_bot()
