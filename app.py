from flask import Flask, request
from flask_cors import CORS
from format import clang_format

app = Flask(__name__)
CORS(app, supports_credentials=True)

@app.route('/format', methods=['POST'])
def format():
    data = request.data.decode('utf-8')
    return clang_format(data)


if __name__ == "__main__":
    app.run(debug=True, port=10245, host='0.0.0.0')
