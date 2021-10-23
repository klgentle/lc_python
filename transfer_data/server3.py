from flask import Flask, Response, jsonify, json

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello, World!</h1>", {"Content-Type": "text/html"}


@app.route("/data")
def get_data2():
    return jsonify({"foo": "bar"})


@app.route("/transfer_data")
def transfer_data():
    html_content = ""
    with open("test.html", "r") as f:
        html_content = f.read()
    return app.response_class(
        json.dumps(html_content), status=200, mimetype="application/json"
    )


if __name__ == "__main__":
    app.run(host="192.168.5.201", port=8000, debug=True)
