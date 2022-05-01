import sys
sys.path.append('.')
import pandas as pd
from sqlalchemy import create_engine 


if __name__ == "__main__":
    data = pd.read_csv(f'./컴소과.csv')
    engine = create_engine("postgresql://postgres:postgres@postgres:5432/crawled_data", convert_unicode = False, connect_args={'connect_timeout': 3})
    conn = engine.connect()
    data.to_sql(name='noti',con = conn, if_exists='replace')
    with conn as con:
        con.execute("Alter table noti add primary key (index);")
    conn.close()