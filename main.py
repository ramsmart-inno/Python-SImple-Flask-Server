import time
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/")
def token_trigger():
    return jsonify('We processed Your request'), 200


@app.route("/<int:name>")
async def token(name: int):
    i = 0
    while i < name:
        i += 1
        time.sleep(3)
        print('little')

    return jsonify('We processed Your request ' + str(name)), 200


@app.route("/<string:na>")
async def tok(na: str):
    return jsonify('We processed Your request ' + na), 200

if __name__ == "__main__":
    app.run(port=5463)
