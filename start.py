# -*- coding: utf-8 -*-

from flask import Flask
import pandas as pd
from sqlalchemy import create_engine
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


def db_select(choice,choice1):
    list=[]
    # choice="\'생활비지원'"
    # choice1="\'%%대학생%%'"
    result= engine.execute("SELECT name FROM dreamspon WHERE advantage LIKE {0} AND who like {1} ".format(choice,choice1))  
    for r in result:
        list.append(str(r))
       
   
    print(list[1])
    print(list[2])
    return list


app = Flask(__name__)

@app.route("/")
def index():
    # db_create()
    return "Hello World!"


if __name__ == "__main__":
    db_create()
    # db_select()