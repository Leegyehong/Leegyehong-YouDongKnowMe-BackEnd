import firebase_admin
from firebase_admin import credentials
from firebase_admin import messaging

cred = credentials.Certificate("./dmu-crawling/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

def send_to_firebase_cloud_messaging():
    # This registration token comes from the client FCM SDKs.
    #registration_token = 'dV_frwRzSB21yx6pFOtZWS:APA91bHCv95X0UTWo-X7gF_uJ1NlJTBOy6UDNris5bDKwbLChZ1B8Ccv-8gKyj4x2-OVwdduBz-yz0uHCMzETnuO2kEKH_xzZa_spynCh1ttBMWaHx7ajfF5O-brxuXz-p_Wv3ES0jDj'
    topic = 'weather'

    # See documentation on defining a message payload.
    message = messaging.Message(
        notification=messaging.Notification(
            title='김정호 스타좁밥',
            body='테사기 뺴애애애액',
        ),
        # token=registration_token,
        topic = topic,
    )

    response = messaging.send(message)
    # Response is a message ID string.
    print('Successfully sent message:', response)
    

send_to_firebase_cloud_messaging()