
from flask import Flask
from flask import request

app = Flask(__name__)

from model.rnn_shakespeare import predict, restore_model

unique_chars, predictions, sess, x, len_unique_chars = restore_model('./model/shakespeare.txt',
                                                                     './model/tmp/rnn_model59.ckpt')

@app.route("/")
def hello():
    return "Hello World!"


@app.route('/complete', methods=['POST'])
def complete():
    if request.method == 'POST':
        text_input = request.form['text']
        text_output = predict(text_input, unique_chars, predictions, sess, x, len_unique_chars)
        return text_output


if __name__ == '__main__':
    # uncomment below line if hosting
    # app.run(host='YOUR IP HERE', port=8080)
    app.run()

