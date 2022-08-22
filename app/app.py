# -*- coding: utf-8 -*-

from flask import Flask
import pandas as pd
from sqlalchemy import create_engine


## DB 연결 Local
def db_create():
    #로컬
    # engine = create_engine("postgresql://postgres:12232305@localhost:5432/postgres",echo=False)
    # postgresql://username:password@localhost:5432/Maintenance database
    #Heroku
    engine = create_engine("postgresql://tojvmfkykntpsj:b6f38303928fbc29ae4debc556f872a08434cc7bc943ad3f7feec76b7d66926d@ec2-54-86-106-48.compute-1.amazonaws.com:5432/dbtl4309937sq8", echo = False)

    engine.connect()
    engine.execute("""
        CREATE TABLE IF NOT EXISTS iris(
            sepal_length FLOAT NOT NULL,
            sepal_width FLOAT NOT NULL,
            pepal_length FLOAT NOT NULL,
            pepal_width FLOAT NOT NULL,
            species VARCHAR(100) NOT NULL
        );"""
    )
    data = pd.read_csv('data/dreamspon.csv')
    print(data)
    data.to_sql(name='dreamspon', con=engine, schema = 'public', if_exists='replace', index=False)

app = Flask(__name__)

@app.route("/")
def index():
    # db_create()
    return "Hello World!"


if __name__ == "__main__":
    db_create()
    app.run()