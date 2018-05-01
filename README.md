# The Writing Fool

The Writing Fool is a writing style transfer creativity supporting tool. 

# How to Run it

## To run the Writing Fool web application:

* Install the style27 anaconda environment using the environment.yml file provided in the root directory.
* Add your Tensorflow model checkpoints of both predictive and style transfer text in a data folder under the root directory. 
For exact folder structure needed for this directory, please see the model related lines in server.py. 
Also add a preprocessing object of your preprocessed text, and the word embedding used by
the model in the same data directory.
* Choose which author's style you which to enable by commenting/uncommenting out the necessary model learning code in server.py. 
Current Writing Fool does not support showing multiple author's style at the same time.
* With Flask installed and the style27 environment turned on, run `python server.py` command in terminal.
* On the default setting you should be able to go to http://127.0.0.1:5000 to use/see the tool

## To run the sentence completion tool:
* First, train your model via the Language-RNN notebook in model, it'll save its models in the model/tmp directory
* Then update rnn.py with the name of the model you want to use. 
* Install Flask, then run `python rnn.py`
* On default setting, you need to send POST requests to http://127.0.0.1:8080 with a form body with the 'text' attribute
set to the sentence you wish to complete and get a completed sentence in return. 

  