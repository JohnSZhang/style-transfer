from flask import Flask
from flask import render_template
from flask import request

from model.code.main.load_model_demo import PreProcessing as prepro
from model.code.main.load_model_demo import Demo

app = Flask(__name__)

demo = Demo()
demo.loadModel("data/pointer_model7.ckpt")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/inference', methods=['POST'])
def inference():
    if request.method == 'POST':
        text_input = request.form['text']
        text_input = text_input.split("\n")
        print 'new text input:', text_input
        return demo.getOutput(text_input)




