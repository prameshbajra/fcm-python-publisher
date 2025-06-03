import concurrent.futures
from firebase_admin import credentials, initialize_app, messaging
import traceback
import json

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

print("\n🛠️ Building notification messages...")

device_tokens = [
    'XXXXX',
    'YYYYY'
]

tasks = []
results = []  # Track success/failure info

try:
    for idx, token in enumerate(device_tokens, start=1):
        notification = messaging.Notification(
            title="Money SMS - Update your app",
            body="Your version of Money SMS is outdated. Please update it.",
        )

        message = messaging.Message(
            notification=notification,
            data={},
            token=token,
        )

        tasks.append((idx, token, message))
        print(f"📝 Prepared notification {idx} for token ending with ...{token[-5:]}")

except Exception as e:
    print("❌ Error while preparing notifications.")
    traceback.print_exc()
    exit(1)


def send_notification(index, token, message):
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
        return (index, token, True, response)

    except Exception as e:
        print(f"❌ Error while sending notification {index}:")
        traceback.print_exc()
        return (index, token, False, str(e))


print("\n⚙️ Starting concurrent notification sending...")

with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = [executor.submit(send_notification, i, token, msg) for i, token, msg in tasks]
    for future in concurrent.futures.as_completed(futures):
        results.append(future.result())


print("\n📋 Notification Delivery Summary:")
for index, token, success, info in results:
    status = "✅ SUCCESS" if success else "❌ FAILED"
    print(f"{status} - Token : {token} | Info: {info}")

print("\n🎉 All notifications processed.")