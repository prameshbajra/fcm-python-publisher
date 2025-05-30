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
# 📦 Create Messaging Tasks (One Per Message)
# ─────────────────────────────────────────────────────
print("\n🛠️ Building individual messages...")

tasks = []

try:
    for i in range(100, 101):
        message = messaging.Message(
            data={
                'testId': f'{i}335971',
                'destination': '+4916092482967',
                'text': f'{i}',
                'simSlot': '0',
                'simId': 'SimOne',
                'type': 'sentSms'
            },
            token='eyJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJ7XCJ1c2VySWRcIjoxMTI2MzI2LFwicm9sZVwiOlwiTU9ORVlfU01TX1VTRVJcIn0iLCJpc3MiOiJpZGVudGl0eSIsImlhdCI6MTc0ODYwOTg4NiwiZXhwIjoxNzQ5MjE0Njg2fQ.fUB-1XDiXW35ly3yeEYpF5B7ICbBxwemj9Ldws8sw7ZMLJ5otmdd9kN46Jz_VwJQBbMlfHQHUT-QOrA7QszHsH_qH0lLfEIHrxsR95JAhDZ3cSf-6GivWyy5DyNYFhgfneCe8saUOzzm2C6UAAm37knY-mtyb4fx4GMEP05BUWqsTBFhfAU7XTa7UoJN9LcUI1J_C7_0AqVnnpatLjZ7SAb-UNojt949VeOcJkeIkgpFwMqq4kDFLWuVgNiIaBQpAbolruG4DLniAfQ9tQUBqBGDZpZrt_FJuJP2oXDS48gMfZEg45te4mIpM4OA__B6qt4udGPm4JMpjmrjLMu-TA',
        )
        tasks.append((i, message))
        print(f"📝 Prepared message {i} with testId {i}335971")

except Exception as e:
    print("❌ Error while preparing messages.")
    traceback.print_exc()
    exit(1)

# ─────────────────────────────────────────────────────
# 🚀 Define Message Sender Function
# ─────────────────────────────────────────────────────
def send_message(index, message):
    try:
        print(f"\n📤 Sending message {index}:")
        print(json.dumps(message.data, indent=2))

        response = messaging.send(message)

        print(f"✅ Message {index} sent successfully! Message ID: {response}")
        print("-" * 50)

    except Exception as e:
        print(f"❌ Error while sending message {index}:")
        traceback.print_exc()

# ─────────────────────────────────────────────────────
# 🧵 Send Messages Using ThreadPool (Parallel Execution)
# ─────────────────────────────────────────────────────
print("\n⚙️ Starting concurrent message sending...")

with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = [executor.submit(send_message, i, msg) for i, msg in tasks]
    concurrent.futures.wait(futures)

print("\n🎉 All messages processed.")