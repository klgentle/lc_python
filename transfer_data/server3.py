import sqlite3
from flask import Flask, Response, jsonify, json, request
from exchangelib import Credentials, Configuration, Account, DELEGATE, Mailbox, UTC, Message
from exchangelib.protocol import BaseProtocol, NoVerifyHTTPAdapter, FaultTolerance
from exchangelib.util import PrettyXmlHandler
import logging
import urllib3

logging.basicConfig(level=logging.DEBUG, handlers=[PrettyXmlHandler()])


app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Hello, World!</h1>", {"Content-Type": "text/html"}


@app.route("/data")
def get_data2():
    return jsonify({"foo": "bar"})


@app.route("/RPM_transfer_data/transfer_data/<site_name>")
def transfer_data(site_name):
    print(query_data(site_name))
    return app.response_class(
        json.dumps(query_data(site_name)), status=200, mimetype="application/json"
    )


@app.route("/RPM_transfer_data/receive_data/<site_name>", methods=["POST"])
def receive_data(site_name):
    print("site_name", request.form.get("site_name"))
    print("site_data", request.form.get("site_data"))
    save_data([request.form.get("site_name"), request.form.get("site_data")])
    return "data save successful."


def save_data(site_data):
    # 若不存在则创建
    con = sqlite3.connect("ifrs9.db")
    try:
        # 游标对象
        cur = con.cursor()
        # 新建表
        cur.execute(
            "create table if not exists ifrs9_data \
             (site_name text primary key not null, site_data text)"
        )
        cur.execute("delete from ifrs9_data where site_name=?", (site_data[0],))
        # insert data
        cur.execute(
            "INSERT INTO ifrs9_data(site_name, site_data) VALUES(?,?)",
            (site_data[0], site_data[1]),
        )
        cur.execute("select * from ifrs9_data")
        print(cur.fetchall())
        print("data save successful.")

        con.commit()
    finally:
        con.close()


@app.route("/RPM_transfer_data/query_data/<site_name>")
def query_data(site_name):
    # 若不存在则创建
    con = sqlite3.connect("ifrs9.db")
    try:
        # 游标对象
        cur = con.cursor()
        cur.execute("select * from ifrs9_data where site_name=?", (site_name,))
        query_result = cur.fetchall()
    finally:
        con.close()

    print(query_result)
    if not query_result:
        return "failed"
    return query_result[0][1]


@app.route("/RPM_transfer_data/send_mail_ex/<site_name>")
def send_mail_ex(site_name):
    BaseProtocol.HTTP_ADAPTER_CLS = NoVerifyHTTPAdapter
    urllib3.disable_warnings()

    credentials = Credentials(username="klgentle4@outlook.com", password="ol654321")
    config = Configuration(server="outlook.office365.com", credentials=credentials)

    my_account = Account(
        primary_smtp_address="klgentle4@outlook.com",
        credentials=credentials,
        config=config,
        access_type=DELEGATE,
        default_timezone=UTC,
    )
    m = Message(
        account=my_account,
        subject="Daily motivation",
        body="All bodies are beautiful",
        to_recipients=[Mailbox(email_address="klgentle4@outlook.com")],
    )
    m.send()
    return "Success"


if __name__ == "__main__":
    app.run(host="192.168.5.201", port=8000, debug=True)
    # ("HASE", "1,HASE,12312,Oct,22,22:46,123\n2,HSCN,12312,Oct,22,22:46,123\n3,HMO,12312,Oct,22,22:46,123"),
#    curl http://192.168.5.201:8000/RPM_transfer_data/receive_data/HASE -X POST -d 'site_name=HASE' -d "site_data=1,HASE,12312,Oct,22,22:46,123
# 2,HSCN,12312,Oct,22,22:46,123
# 3,HMO,12312,Oct,22,22:46,123"
#
# curl http://192.168.5.201:8000/RPM_transfer_data/transfer_data/HASE

# echo -e "1,HASE,12312,Oct,22,22:46,123\n2,HSCN,12312,Oct,22,22:46,123\n3,HMO,12312,Oct,22,22:46,123" | grep HASE
