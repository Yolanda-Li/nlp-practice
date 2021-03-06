from api.similar_score import show_similar_score
from keras.models import load_model
from flask_environments import Environments
from flask import Flask
import tensorflow as tf
import json

from ImageNet_model import create_siamese
input_shape = (224,224,3)


app = Flask(__name__, static_folder='static')  #创建flask对象


env = Environments(app)  #配置
env.from_object('config')
graph = None
siamese_model = None


def load_siamese_model():
    """Load the trained model."""
    global graph
    graph = tf.get_default_graph()  #获得默认图
    global siamese_model,siamese_model_pic
    siamese_model = load_model(app.config['SIAMESE_MODEL_FILE'])
    siamese_model_pic = create_siamese(input_shape)
    siamese_model_pic.load_weights(app.config['SIAMESE_MODEL_PIC_FILE'])


@app.route("/eval", methods=['POST'])  #限制url请求方式，post参数获取是通过request.form['传进来的参数']取到
def predict_result():
    """Get the articles and its similar degree."""
    score = show_similar_score(graph, siamese_model_pic)
    return json.dumps(score)  #将dict类型的数据转成str


if __name__ == "__main__":
    load_siamese_model()
    app.run(host=app.config['HOST'], port=app.config['PORT'], debug=app.config['DEBUG'])
