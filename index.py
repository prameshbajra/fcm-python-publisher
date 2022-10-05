from firebase_admin import credentials, initialize_app, messaging

cred = credentials.Certificate(
    '/Users/prameshbajracharya/lecodage/telq/fcm-python/money-sms-8be6c-firebase-adminsdk-cgx7z-8fe77738aa.json'
)
app = initialize_app(cred)

print('PROJECT ID: ', app.project_id)

message = messaging.MulticastMessage(
    data={
        'location': 'Hamburg, Germany',
        'company': 'TelQ',
        'app': 'money_sms_app',
        'destination': '+9779841623204',
        'text': 'Hey there. This is MO testing sample.'
    },
    tokens=[
        'dlLfrfJ2SpCc5VsN1P-PEU:APA91bF_wUMSWTr5IB45cqhdJTF6KRl_Krcd0Jypc-bkKuq7BbE1tsS-gIy8F1sldJEqocppurMegAqdrGil7R4nPk1ZXsDBHuczZ7d_lV5SpHEqKhAq-fXRO494gTVUlsuXAolioJFR',
    ])

message_response = messaging.send_multicast(multicast_message=message)
print(message_response)

print('Failure Count : ', message_response.failure_count)
print('Responses (Probably not of any use): ', message_response.responses)
