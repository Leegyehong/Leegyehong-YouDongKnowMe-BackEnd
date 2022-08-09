import firebase_admin
from firebase_admin import credentials
from firebase_admin import messaging

cred = credentials.Certificate("./dmu-crawling/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

def send_to_firebase_cloud_messaging():
    # This registration token comes from the client FCM SDKs.
    #registration_token = 'cdqgXE8IRJ2mkhbo9Qld2x:APA91bF3aQMyO87ZthR92VfOsdpg5ITKIUh9wOalHXl1SwfrtwCWAqOdOrrOxxUqgFDSQ5wSm0bk5kkO8NgKod1Iyi5SE14PXqFPAvcvisJphSKA8stZ-7cEpwUaHitXW2yadVOD8W8e'
    
    # TODO : 함수에서 파라미터를 받아서 해당 변수에 주입 필요 
    major_code = '1'
    num = '3597'
    title = '전자출결 푸시(PUSH) 서비스 운영에 따른 전자출결 앱 업데이트 안내'
    keyword = 'exam'

    message = messaging.Message(
        data={
            'major_code': major_code,
            'num': num,
            'title': title,
            'keyword': keyword
        },
        topic = keyword,
    )

    response = messaging.send(message)

    print('Successfully sent message:', response)


send_to_firebase_cloud_messaging()