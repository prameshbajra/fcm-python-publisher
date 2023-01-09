import concurrent.futures
from firebase_admin import credentials, initialize_app, messaging

cred = credentials.Certificate(
    '/Users/prameshbajracharya/lecodage/telq/fcm-python/money-sms-8be6c-firebase-adminsdk-cgx7z-8fe77738aa.json'
)
app = initialize_app(cred)

print('PROJECT ID: ', app.project_id)

tasks = []

for i in range(100, 103):
    message = messaging.MulticastMessage(
        data={
            'testId': f'{i}335971',
            'destination': '9779813457822',
            'text': f'{i}-TP-5971',
            'simSlot': '0',
            'simId': 'SimOne',
            'type': 'sentSms'
        },
        tokens=[
            'cGpJ-f5AR5ez8t7nP87gVr:APA91bGjyom_rbN_0JBTMZDL5etebyKS0p5k43pm8FukUL1IIqokUaQ9AmHuiF4nu39ZOo60iHdJ3hPIcPO0nC9nhv-hzMZTddohcqiWdRBY3I2LBEFxxNxHgz4mW8tcTWnm3EXN89nQ',
        ])

    tasks.append(message)


def send(message):
    print("SEND : ", message)
    message_response = messaging.send_multicast(multicast_message=message)
    print(message_response)
    print('Failure Count : ', message_response.failure_count)
    print('Responses (Probably not of any use): ', message_response.responses)
    print('----------')


with concurrent.futures.ThreadPoolExecutor() as executor:
    # Start the tasks
    results = [executor.submit(send, task) for task in tasks]

    # Wait for the tasks to complete
    concurrent.futures.wait(results)
