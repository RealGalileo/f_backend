import pymysql
from flask import Flask
from flask_cors import CORS
import config

app = Flask(__name__)
app.config["DEBUG"] = True
app.config['JSON_AS_ASCII'] = False
CORS(app)


def connect():
    connection = pymysql.connect(host=config.host,
                                 port=config.port,
                                 user=config.user,
                                 password=config.password,
                                 database=config.database)
    return connection


def build_dict(description, content):
    return dict(zip([x[0] for x in description], [x for x in content]))


@app.route("/show_all")
def show_all():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM match_info')
    record_list = list(map(lambda content: build_dict(cursor.description, content), cursor.fetchall()))
    conn.close()
    return record_list


if __name__ == "__main__":
    table = show_all();
    for i in table:
        print(i);

