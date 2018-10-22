from keras.models import load_model
from flask_environments import Environments
from flask import Flask
import tensorflow as tf
import json
import sys
sys.path.append("/api")
from api.similar_score import show_similar_score


app = Flask(__name__, static_folder='static')  #Create a flask object


env = Environments(app)  #config
env.from_object('config')
graph = None
siamese_model = None


def load_siamese_model():
    """Load the trained model."""
    global graph
    graph = tf.get_default_graph()  #Get the default map
    global siamese_model
    siamese_model = load_model(app.config['SIAMESE_MODEL_FILE'])


@app.route("/eval", methods=['POST'])
def predict_result():
    """Get the articles and its similar degree."""
    score = show_similar_score(graph, siamese_model)
    print(json.dumps(score))
    return json.dumps(score)  #Convert dict type data to str


if __name__ == "__main__":
    load_siamese_model()
    app.run(host=app.config['HOST'], port=app.config['PORT'], debug=app.config['DEBUG'])
