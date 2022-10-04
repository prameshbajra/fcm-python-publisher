from firebase_admin import credentials, initialize_app, messaging

cred = credentials.Certificate('/Users/prameshbajracharya/lecodage/telq/fcm-python/backgroundfcm-telq-firebase-adminsdk-jtfoz-799bd45280.json')
app = initialize_app(cred)

print('PROJECT ID: ', app.project_id)

message = messaging.MulticastMessage(
    data={
        'location': 'Hamburg, Germany',
        'company': 'TelQ',
        'app': 'money_sms_app'
    },
    tokens=[
        'dvgVX0iiSU6dzrfDRVueRf:APA91bFjVLoZjUIzyXruJIwyDDtdSjhCeyfSdplnBJ8szLb4GkRgzoVQw033slOYeSrnMlBkqxUA5IOuU4eOsQovYqrQiwBK79ul2Z-9HnyT6SbkyqmTeg4BBrFybojs3mZv3PmLYG_z',
        'dK2xbUuLQYGbhnAqXzypFp:APA91bHB6YXJA4OkXEfmbEhm_-CRCZZCuQUiH8ssl1_YAXgWjtTp9evM2dKMY-o9NsWuZ217S_g8gN96PfPijCiQhk9VSQGCXmkPsGGBJpKgZwH3UlaiDsYvEieifozTdfP5Pa_6jF7p'
    ])

message_response = messaging.send_multicast(multicast_message=message)
print(message_response)