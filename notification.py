import concurrent.futures
from firebase_admin import credentials, initialize_app, messaging
import traceback
import json

# ─────────────────────────────────────────────────────
# 🔐 Initialize Firebase App with Credentials
# ─────────────────────────────────────────────────────
print("🔐 Initializing Firebase app...")

try:
    cred_path = '/Users/prameshbajra/Entwicklung/fcm-python-publisher/money-sms-8be6c-firebase-adminsdk-cgx7z-a2c184b31a.json'
    cred = credentials.Certificate(cred_path)
    app = initialize_app(cred)

    print("✅ Firebase app initialized successfully!")
    print("🔍 Project ID:", app.project_id)

except Exception as e:
    print("❌ Failed to initialize Firebase app.")
    traceback.print_exc()
    exit(1)

# ─────────────────────────────────────────────────────
# 📦 Create Push Notification Tasks
# ─────────────────────────────────────────────────────
print("\n🛠️ Building notification messages...")

tasks = []

try:
    for i in range(1, 2):  # Adjusted range to send only 1 notification
        notification = messaging.Notification(
            title=f"🔥 Alert #{i}",
            body=f"This is a push notification #{i}",
            image="https://example.com/image.png"  # Optional
        )

        message = messaging.Message(
            notification=notification,
            data={},
            token='ePy3jW91RW26AVZ1ajOWVv:APA91bGzeewZnCOz1rtK-dvQLG1xT6iQAstGeDZIzNp4kvY5nZzcJlS8iKVZZH0HsK-Nr3ZdzQFRZqJbjGbcQWMxToRHUVc0zc0H_JJ5AfvLW6-0FxyEjtY',
        )

        tasks.append((i, message))
        print(f"📝 Prepared notification {i}")

except Exception as e:
    print("❌ Error while preparing notifications.")
    traceback.print_exc()
    exit(1)

# ─────────────────────────────────────────────────────
# 🚀 Define Notification Sender Function
# ─────────────────────────────────────────────────────
def send_notification(index, message):
    try:
        print(f"\n📤 Sending notification {index}:")
        print(json.dumps({
            'title': message.notification.title,
            'body': message.notification.body,
            'data': message.data
        }, indent=2))

        response = messaging.send(message)

        print(f"✅ Notification {index} sent successfully! Message ID: {response}")
        print("-" * 50)

    except Exception as e:
        print(f"❌ Error while sending notification {index}:")
        traceback.print_exc()

# ─────────────────────────────────────────────────────
# 🧵 Send Notifications Concurrently
# ─────────────────────────────────────────────────────
print("\n⚙️ Starting concurrent notification sending...")

with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = [executor.submit(send_notification, i, msg) for i, msg in tasks]
    concurrent.futures.wait(futures)

print("\n🎉 All notifications processed.")