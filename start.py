# -*- coding: utf-8 -*-

from flask import Flask
import pandas as pd
from sqlalchemy import create_engine
import psycopg2

engine = create_engine("postgresql://oorbpqoyofkzzz:cf8f09e5eb71660cfca525b431d2029c9753ca80962c0f9f8241192dca533481@ec2-52-207-15-147.compute-1.amazonaws.com:5432/dejcqpc36a8hi6", echo = False)

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


def area_db(naming):
# 입력된 이름이 포함된 행을 불러오는 함수
    conn = psycopg2.connect(host="ec2-52-207-15-147.compute-1.amazonaws.com", dbname="dejcqpc36a8hi6", user="oorbpqoyofkzzz", password="cf8f09e5eb71660cfca525b431d2029c9753ca80962c0f9f8241192dca533481")
    # heroku에 배포되어 있는 데이터베이스에 접속하기
    cur = conn.cursor()
    # cursor = 임시 객체생성
    # 생성된 임시객체를 cur에 저장
    #name = "\'월성장학회 주변지역 장학'"
    cur.execute("SELECT name, url, image FROM dreamspon WHERE name LIKE '%%{}%%';".format(naming))
    # sql문장을 실행할 수 있게 해주는 메서드
    # name 컬럼에 naming이 포함되는 행 출력해주는 쿼리
    rows = cur.fetchall() 
    # 데이터내용 전부 불러서 rows에 입력
    # list 타입
    df = pd.DataFrame(rows, columns = ['name', 'url', 'image'])
    #print(df)
    # DataFrame으로 만들어주기
    # 컬럼명을 지정
    return df
