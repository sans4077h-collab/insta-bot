from instagrapi import Client
import time
import os

# --- 1. البيانات (تأكد من كتابة الباسوورد الجديد) ---
USERNAME = "sans_7_4"
PASSWORD = "ksmk123456" 
GROUP_ID = "949847180867720"
MESSAGE = "احدهم يجرب"  
"

# اسم ملف الجلسة لحفظ تسجيل الدخول
SESSION_FILE = "session.json"

cl = Client()

def start_bot():
    try:
        # محاولة تحميل الجلسة السابقة لتجنب قفل الحساب
        if os.path.exists(SESSION_FILE):
            print("📦 تحميل الجلسة المحفوظة...")
            cl.load_settings(SESSION_FILE)
        
        print(f"📡 محاولة تسجيل الدخول لـ: {USERNAME}")
        cl.login(USERNAME, PASSWORD)
        
        # حفظ الجلسة بعد نجاح الدخول لأول مرة
        cl.dump_settings(SESSION_FILE)
        print("✅ تم تسجيل الدخول وحفظ الجلسة بنجاح!")

        while True:
            try:
                # إرسال الرسالة
                cl.direct_send(MESSAGE, thread_ids=[GROUP_ID])
                print(f"✅ تم إرسال الرسالة بنجاح.")
                
                # الانتظار 20 دقيقة
                print("😴 سأنتظر 20 دقيقة قبل الرسالة القادمة...")
                time.sleep(220)
                
            except Exception as e:
                print(f"❌ خطأ أثناء الإرسال: {e}")
                time.sleep(60)

    except Exception as e:
        print(f"❌ فشل تسجيل الدخول: {e}")

if __name__ == "__main__":
    start_bot()
