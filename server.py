from flask import Flask
from flask import render_template
from flask import request
import tensorflow as tf

from model.code.main.load_model_demo import PreProcessing as prepro
from model.code.main.load_model_demo import Demo
from model.rnn_shakespeare import predict, restore_model

app = Flask(__name__)

g1 = tf.Graph()
g2 = tf.Graph()
g3 = tf.Graph()
g4 = tf.Graph()

with g1.as_default():
    shakespeare_style_model = Demo()
    shakespeare_style_model.loadModel("./data/style_transfer/shakespeare/pointer_model7.ckpt",
                                      preprocess_path="./data/style_transfer/shakespeare/",
                                      embed_name = 'retrofitted_external_192_startend.p',
                                      cell_size = 192)
with g2.as_default():
    shakespeare_text_data = restore_model('./data/predictive_models/shakespeare/shakespeare.txt',
                                          './data/predictive_models/shakespeare/rnn_model59.ckpt')
# with g3.as_default():
#     austen_style_model = Demo()
#     austen_style_model.loadModel("./data/style_transfer/austen/pointer_model10.ckpt",
#                                  preprocess_path="./data/style_transfer/austen/",
#                                  embed_name = 'retrofitted_external_192_startend.p',
#                                  cell_size = 192)
#
# with g4.as_default():
#     austen_text_data = restore_model('./data/predictive_models/austen/p_and_p.txt',
#                                     './data/predictive_models/austen/rnn_model29.ckpt')


def padUp(line,finalLength,paddingMethod):
    words=line.split()
    words=["<s>",]+words+["</s>",]
    lineLength=len(words)
    padLength=finalLength-lineLength
    if padLength>0:
        if paddingMethod=="pre":
            words=["<p>"]*padLength+words
        elif paddingMethod=="post":
            words=words+["<p>",]*padLength
    elif padLength<0:
        words=words[:finalLength]

    return words

def copy_mechanism(input, output, alpha):
    inputLines = [padUp(line, 25, "pre") for line in input]
    hypLines = [padUp(line, 24, "post") for line in output]
    outputLines = []

    for i in range(len(inputLines)):
        hypLine=hypLines[i]
        inpLine=inputLines[i]
        attentionMatrix=alpha[i]

        inputStartIndex=-1
        for x in inpLine:
            if x != "<p>":
                break
            else:
                inputStartIndex += 1

        hypEndIndex = 0

        for x in hypLine:
            if x == "<p>":
                break
            else:
                hypEndIndex += 1

        hypLine=hypLine[:hypEndIndex]
        inpLine=inpLine[inputStartIndex+1:]

        attentionMatrix = attentionMatrix[:hypEndIndex,inputStartIndex+1:]
        newHypLine = []

        for k, x in enumerate(hypLine):

            if x == "<s>" or x == "</s>":
                continue
            elif x != "unk":
                newHypLine.append(x)
            else:
                attentionList=list(attentionMatrix[k])
                maxAttention=max(attentionList)
                maxAttentionIndices=[j for j,a in enumerate(attentionList) if a==maxAttention]
                maxAttentionIndex=maxAttentionIndices[0]
                xNew=inpLine[maxAttentionIndex]
                newHypLine.append(xNew)

        outputLines.append((" ").join(newHypLine))
    return outputLines


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/inference', methods=['POST'])
def inference():
    if request.method == 'POST':
        text_input = request.form['text']
        text_input = text_input.split("\n")
        print 'new text input:', text_input
        text_output, alpha = shakespeare_style_model.getOutput(text_input)
        outputs = copy_mechanism(text_input, text_output, alpha)
        return ('\n').join(outputs)


@app.route('/complete', methods=['POST'])
def complete():
    if request.method == 'POST':
        print 'received post'
        text_input = request.form['text']
        unique_chars, predictions, sess, x, len_unique_chars = shakespeare_text_data
        text_output = predict(text_input, unique_chars, predictions, sess, x, len_unique_chars)
        return text_output


if __name__ == '__main__':
    # Uncomment below line if hosting
    # app.run(host='128.61.105.147', port=5000)
    app.run()



