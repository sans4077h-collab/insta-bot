from instagrapi import Client
import time

# --- البيانات (تأكد من كتابتها يدوياً داخل علامات التنصيص) ---
USERNAME = "sans_7_4"
PASSWORD = "ksmk12345" # <--- حط باسورده الحقيقي هنا
GROUP_ID = "949847180867720"
MESSAGE = "احدهم يجرب"

cl = Client()

def login_and_send():
    try:
        # تنظيف اسم المستخدم من أي مسافات
        user = USERNAME.strip()
        print(f"📡 المحاولة الآن لليوزر: [{user}]")
        
        # تسجيل الدخول
        cl.login(user, PASSWORD)
        print("✅ تم تسجيل الدخول بنجاح!")
        
        while True:
            try:
                cl.direct_send(MESSAGE, thread_ids=[GROUP_ID])
                print("✅ تم إرسال الرسالة")
                time.sleep(220) # كل 20 دقيقة
            except Exception as e:
                print(f"❌ خطأ أثناء الإرسال: {e}")
                time.sleep(60)
                
    except Exception as e:
        print(f"❌ فشل الدخول: {e}")
        print("💡 نصيحة: إذا كنت متأكد من اليوزر والباسورد، افتح تطبيق إنستغرام بجوالك وسجل خروج ثم دخول مرة ثانية لتنشيط الحساب.")

if __name__ == "__main__":
    login_and_send()
