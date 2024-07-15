from flask import Flask, jsonify, request


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():  # put application's code here
    if request.method == "POST":
        print('POST')
        print(request.json)
        return jsonify(message="receive your data bb")
    else:
        return jsonify(message="Hello World!")


if __name__ == '__main__':
    app.run()
