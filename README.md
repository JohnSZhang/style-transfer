# The Writing Fool

The Writing Fool is a writing style transfer creativity supporting tool. 

# How to Run it

## To run the main tool:
* Make sure you have TensorFlow v1.1.0 and above installed
* Add your Tensorflow model checkpoints, 
a preprocessing object of your preprocessed text, and the word embedding used by
the model in the data directory.
* modify model/code/main/load_model_demo.py accordingly to the model checkpoint you want to use.
* Install Flask, then run `python server.py`
* On the default setting you should be able to go to http://127.0.0.1:500 to see the tool

## To run the sentence completion tool:
* First, train your model via the Language-RNN notebook in model, it'll save its models in the model/tmp directory
* Then update rnn.py with the name of the model you want to use. 
* Install Flask, then run `python rnn.py`
* On default setting, you need to send POST requests to http://127.0.0.1:8080 with a form body with the 'text' attribute
set to the sentence you wish to complete and get a completed sentence in return. 

  