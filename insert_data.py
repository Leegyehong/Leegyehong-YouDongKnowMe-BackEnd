import os
import sys
sys.path.append('.')
import pandas as pd
from sqlalchemy import create_engine, MetaData, Table
import firebase_admin
from firebase_admin import credentials
from firebase_admin import messaging

cred = credentials.Certificate("./dmu-crawling/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

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

def send_to_firebase_cloud_messaging(major_code, num, title, keyword):
    # This registration token comes from the client FCM SDKs.
    #registration_token = 'cdqgXE8IRJ2mkhbo9Qld2x:APA91bF3aQMyO87ZthR92VfOsdpg5ITKIUh9wOalHXl1SwfrtwCWAqOdOrrOxxUqgFDSQ5wSm0bk5kkO8NgKod1Iyi5SE14PXqFPAvcvisJphSKA8stZ-7cEpwUaHitXW2yadVOD8W8e'
    
    # TODO : 함수에서 파라미터를 받아서 해당 변수에 주입 필요 
    major_code = major_code
    num = num
    title = title
    keyword = keyword

    message = messaging.Message(
        data={
            'major_code': str(major_code),
            'num': str(num),
            'title': title,
            'keyword': keyword
        },
        topic = keyword,
    )

    response = messaging.send(message)

    print('Successfully sent message:', response)



if __name__ == "__main__":

    path = "./dmu-crawling/crawled/noti/20221117"
    file_list = os.listdir(path)
    engine = create_engine("postgresql://postgres:postgres@3.218.107.236:5432/crawled_data", convert_unicode = False, connect_args={'connect_timeout': 3})
    conn = engine.connect()
    noti = Table('noti', MetaData(), autoload=True, autoload_with=engine)

    for file in file_list:
        data = pd.read_csv(f'./dmu-crawling/crawled/noti/{file}')
        #print(data)
        #data.to_sql(name='noti',con = conn, if_exists='append', index=False)
        
        #with conn as con:
        #    con.execute("Alter table noti add primary key (major_code, num);")
        #conn.close()

        noti = Table('noti', MetaData(), autoload=True, autoload_with=engine)
        data = data.where(pd.notnull(data), None)
        for index, row in data.iterrows():
            
            sql = f"""
                select * from noti where major_code={row['major_code']} and num={row['num']}
            """
            result = engine.execute(sql).fetchall()

            if result:
                qr=noti.update().where(noti.c.major_code==row['major_code'], noti.c.num==row['num']).values(
                    major_code=row['major_code'], num=row['num'],title=row['title'], writer=row['writer'], date=row['date'], content=row['content'],img_url=row['img_url'] ,file_url=row['file_url']
                )
                print(qr)
                engine.execute(qr)
            else:
                qr = noti.insert().values(major_code=row['major_code'], num=row['num'],title=row['title'], writer=row['writer'], date=row['date'], content=row['content'],img_url=row['img_url'] ,file_url=row['file_url'])
                engine.execute(qr)
                for i in keyword:
                    if i in row['title']:
                        send_to_firebase_cloud_messaging(row['major_code'], row['num'], row['title'], keyword[i])
                        break     
                
    #data = pd.read_csv(f'./dmu-crawling/crawled/schedule/학교_학사일정.csv')
    #data.to_sql(name='schedule',con = conn, if_exists='append', index= False)
    conn.close()


    
    