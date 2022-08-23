# -*- coding: utf-8 -*-

from flask import Flask
import pandas as pd
from sqlalchemy import create_engine
import psycopg2

engine = create_engine("postgresql://tojvmfkykntpsj:b6f38303928fbc29ae4debc556f872a08434cc7bc943ad3f7feec76b7d66926d@ec2-54-86-106-48.compute-1.amazonaws.com:5432/dbtl4309937sq8", echo = False)

engine.connect()


def db_create():
    engine.execute("""
        CREATE TABLE IF NOT EXISTS dreamspon(
            name varchar(90) NOT NULL,
            advantage varchar(10) NOT NULL,
            who varchar(40) NOT NULL,
            age varchar(15) NOT NULL,
            where1 VARCHAR(30) NOT NULL,
            qualification VARCHAR(30) NOT NULL,
            url VARCHAR(70) NOT NULL
        );"""
    )
    data = pd.read_csv('data/dreamspon.csv')
    print(data)
    data.to_sql(name='dreamspon', con=engine, schema = 'public', if_exists='replace', index=False)


def db_select(choice):
    list=[]
    # choice="\'%%이름%%'"
    result= engine.execute("SELECT name, url FROM dreamspon WHERE name LIKE '%%{}%%';".format(choice))
    for r in result:
        list.append(str(r))
       
    
    return list


def area_db(naming):
# 입력된 이름이 포함된 행을 불러오는 함수
    conn = psycopg2.connect(host="ec2-54-86-106-48.compute-1.amazonaws.com", dbname="dbtl4309937sq8", user="tojvmfkykntpsj", password="b6f38303928fbc29ae4debc556f872a08434cc7bc943ad3f7feec76b7d66926d")
    # heroku에 배포되어 있는 데이터베이스에 접속하기
    cur = conn.cursor()
    # cursor = 임시 객체생성
    # 생성된 임시객체를 cur에 저장
    #name = "\'월성장학회 주변지역 장학'"
    cur.execute("SELECT * FROM dreamspon WHERE name LIKE '%%{}%%';".format(naming))
    # sql문장을 실행할 수 있게 해주는 메서드
    # name 컬럼에 naming이 포함되는 행 출력해주는 쿼리
    rows = cur.fetchall() 
    # 데이터내용 전부 불러서 rows에 입력
    # list 타입
    df = pd.DataFrame(rows, columns = ['name','url'])
    #print(df)
    # DataFrame으로 만들어주기
    # 컬럼명을 지정
    return df
