
from flask import Flask
from flask import request
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/complete": {"origins": "*"}})

from model.rnn_shakespeare import predict, restore_model

unique_chars, predictions, sess, x, len_unique_chars = restore_model('./model/')
@app.route("/")
def hello():
    return "Hello World!"


@app.route('/complete', methods=['POST'])
def complete():
    if request.method == 'POST':
        text_input = request.form['text']
        print 'new prediction input:', text_input
        text_output = predict(text_input, unique_chars, predictions, sess, x, len_unique_chars)
        return text_output


if __name__ == '__main__':
    app.run(host='128.61.105.147', port=8080)

