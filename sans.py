from instagrapi import Client
import time
import os

# --- البيانات الصحيحة ---
USERNAME = "sans_7_4"  # <--- تأكد أن هذا يوزرك الصحيح
PASSWORD = "ksmk123456" 
GROUP_ID = "949847180867720"
MESSAGE = "احدهم يجرب"

SESSION_FILE = "session.json"
cl = Client()

def start_bot():
    try:
        user = USERNAME.strip()
        
        if os.path.exists(SESSION_FILE):
            print("📦 تحميل الجلسة المحفوظة...")
            cl.load_settings(SESSION_FILE)
        
        print(f"📡 محاولة الدخول لـ: {user}")
        cl.login(user, PASSWORD)
        
        cl.dump_settings(SESSION_FILE)
        print("✅ تم تسجيل الدخول وحفظ الجلسة!")

        while True:
            try:
                cl.direct_send(MESSAGE, thread_ids=[GROUP_ID])
                print(f"✅ تم إرسال: {MESSAGE}")
                print("😴 انتظار 20 دقيقة...")
                time.sleep(220)
                
            except Exception as e:
                print(f"❌ خطأ أثناء الإرسال: {e}")
                time.sleep(60)

    except Exception as e:
        print(f"❌ فشل تسجيل الدخول: {e}")
        print("💡 جرب تفتح الانستقرام وتضغط 'هذا أنا' لو طلع لك تنبيه.")

if __name__ == "__main__":
    start_bot()
