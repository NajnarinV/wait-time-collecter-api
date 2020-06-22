import flask
from flask import request, jsonify
from waitTimeCollector import combine_lists

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return jsonify(combine_lists())

if __name__ == '__main__':
    app.run()