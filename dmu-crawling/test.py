import firebase_admin
from firebase_admin import credentials
from firebase_admin import messaging

cred = credentials.Certificate("./dmu-crawling/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

def send_to_firebase_cloud_messaging():
    # This registration token comes from the client FCM SDKs.
    #registration_token = 'cdqgXE8IRJ2mkhbo9Qld2x:APA91bF3aQMyO87ZthR92VfOsdpg5ITKIUh9wOalHXl1SwfrtwCWAqOdOrrOxxUqgFDSQ5wSm0bk5kkO8NgKod1Iyi5SE14PXqFPAvcvisJphSKA8stZ-7cEpwUaHitXW2yadVOD8W8e'
    topic = 'corona'

    # See documentation on defining a message payload.
    message = messaging.Message(
        data={
            'major_code': '1',
            'num': '120',
            'title' :'[코로나19] 확진자 발생 및 검사시행 안내',
            'topic' : topic
        },
        # notification=messaging.Notification(
        #     title = '등록하신 키워드 알림이 도착했습니다'
        # ),
        #token=registration_token,
        topic = topic,
    )

    response = messaging.send(message)
    # Response is a message ID string.
    print('Successfully sent message:', response)


send_to_firebase_cloud_messaging()