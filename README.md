# The Writing Fool

The Writing Fool is a writing style transfer creativity enchacement tool. 

# How to Run it

To run the server, follow the below steps:
* Make sure you have TensorFlow v1.0.0 and above installed
* Add your Tensorflow model checkpoints in the data directory, 
a preprocessing object of your preprocessed text, and the word embedding used by
the model (and modify model/code/main/load_model_demo.py accordingly).
* Install Flask locally, from the root dir run 
`$ export FLASK_APP=server.py`
and 
`flask run`

  