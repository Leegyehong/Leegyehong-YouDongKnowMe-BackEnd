import os
import sys
sys.path.append('.')
import pandas as pd
from sqlalchemy import create_engine, MetaData, Table


if __name__ == "__main__":

    path = "./dmu-crawling/crawled/"
    file_list = os.listdir(path)
    engine = create_engine("postgresql://postgres:postgres@localhost:5432/crawled_data", convert_unicode = False, connect_args={'connect_timeout': 3})
    conn = engine.connect()
    noti = Table('noti', MetaData(), autoload=True, autoload_with=engine)

    for file in file_list:
        data = pd.read_csv(f'./dmu-crawling/crawled/{file}')
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



