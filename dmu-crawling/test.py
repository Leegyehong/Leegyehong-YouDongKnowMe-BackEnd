import firebase_admin
from firebase_admin import credentials
from firebase_admin import messaging

cred = credentials.Certificate("./dmu-crawling/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

#수업

# 시험 : 시험, 중간고사, 기말고사, 기말, 중간
# 수강 : 수강신청, 정정, OCU, 학점교류, 타학과, 타반, 출석인정, 결시
# 특강 : 특강
# 계절학기 : 계절학기

# 학자금
# 장학 : 장학, 장학금, 미래장학금, 마일리지, 교내장학금
# 국가장학 : 국가근로장학금, 국가장학금, 생활비대출
# 등록 : 등록금

# 학적
# 휴학 : 휴학
# 복학 : 복학
# 졸업 : 졸업
# 전과 : 전과
# 학기포기 : 학기포기

# 취업
# 채용 : 채용
# 공모전 : 공모전
# 현장실습 : 현장실습
# 대회 : 대회
# 봉사 : 봉사

# 기타
# 기숙사 : 기숙사
# 코로나 : 코로나19, 코로나, Covid
# 동아리 : 동아리, Lab
keyword =  {'시험' : 'exam', '중간고사' : 'exam', '기말고사' : 'exam', '기말' : 'exam', '중간' : 'exam',
            '수강신청' : 'course', '정정' : 'course', 'OCU' : 'course', '학점교류' : 'course', '타학과' : 'course', '타반' : 'course', '출석인정' : 'course', '결시' : 'course'
            ,'특강': 'lecture', '계절학기' : 'season',
            '장학' : 'scholarship', '장학금': 'scholarship', '미래장학금': 'scholarship', '마일리지': 'scholarship', '교내장학금': 'scholarship',
            '국가근로장학금' : 'scholarship', '국가장학금' : 'scholarship', '생활비대출' : 'scholarship',
            '등록금' : 'tuition',
            '휴학' : 'leave', '복학' : 'return', '졸업' : 'graduation', '전과':'transfer', '학기포기' : 'drop',
            '채용' : 'recruitment', '공모전':'contest', '현장실습' : 'field', '대회' : 'competition', '봉사' : 'service',
            '기숙사' : 'dormitory', '코로나19' : 'corona', '코로나' : 'corona', 'Covid' : 'corona',
            '동아리' : 'club', 'Lab' : 'club'}

def send_to_firebase_cloud_messaging():
    # This registration token comes from the client FCM SDKs.
    #registration_token = 'cdqgXE8IRJ2mkhbo9Qld2x:APA91bF3aQMyO87ZthR92VfOsdpg5ITKIUh9wOalHXl1SwfrtwCWAqOdOrrOxxUqgFDSQ5wSm0bk5kkO8NgKod1Iyi5SE14PXqFPAvcvisJphSKA8stZ-7cEpwUaHitXW2yadVOD8W8e'
    
    # TODO : 함수에서 파라미터를 받아서 해당 변수에 주입 필요 
    major_code = '1'
    num = '3597'
    title = '전자출결 푸시(PUSH) 서비스 운영에 따른 전자출결 앱 업데이트 안내'
    keyword = 'corona'

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