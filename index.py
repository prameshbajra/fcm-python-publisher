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
    token='dvgVX0iiSU6dzrfDRVueRf:APA91bFjVLoZjUIzyXruJIwyDDtdSjhCeyfSdplnBJ8szLb4GkRgzoVQw033slOYeSrnMlBkqxUA5IOuU4eOsQovYqrQiwBK79ul2Z-9HnyT6SbkyqmTeg4BBrFybojs3mZv3PmLYG_z'
)

message_response = messaging.send(message=message)
print(message_response)