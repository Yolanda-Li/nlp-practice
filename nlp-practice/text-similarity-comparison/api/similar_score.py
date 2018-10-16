from input_handler import create_test_data, data_predict
from config import siamese_config
from flask import request
import uuid
import json
import os


class ConfiGuration(object):
    """Dump stuff here"""


config = ConfiGuration()
config.max_len = siamese_config['MAX_DOCUMENT_LENGTH']
config.data_dir = siamese_config['DATA_DIR']


def show_similar_score(graph, nlp_model):
    """
    Predict the similar degree between two articles.
    :param graph:
    :param nlp_model:
    :return:
        {'similar_score': preds_score}(dict): preds_score(str) is the he similar degree between two articles
    """
    now_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    upload_path = os.path.join(now_path, "data//temp")
    if os.path.exists(upload_path) is False:
        os.makedirs(upload_path)
    w2index_file = os.path.join(config.data_dir, "model//w2index.txt")

    file_1 = request.files['filename1']
    file_2 = request.files['filename2']
    file_1_name = file_1.filename
    file_2_name = file_2.filename

    if file_1_name.endswith('.txt') is False and file_2_name.endswith('.txt') is False:
        return 'only support .txt'

    save_data_dir = os.path.join(upload_path, str(uuid.uuid1()))
    print(save_data_dir)
    os.makedirs(save_data_dir)
    savefile_1 = os.path.join(save_data_dir, file_1_name)
    file_1.save(savefile_1)
    savefile_2 = os.path.join(save_data_dir, file_2_name)
    file_2 .save(savefile_2)

    with open(w2index_file, 'r+', encoding='utf-8') as f:
        w2index = f.read()
    index_dict = json.loads(w2index)

    predict_documents1, predict_documents2 = data_predict(save_data_dir)
    predict_document_pairs = [(x1, x2) for x1, x2 in zip(predict_documents1, predict_documents2)]
    predict_data_x1, predict_data_x2, leaks_predict = create_test_data(index_dict, predict_document_pairs,
                                                                       config.max_len)
    with graph.as_default():
        preds = nlp_model.predict([predict_data_x1, predict_data_x2, leaks_predict], verbose=1).ravel()
    preds_score = str(round(preds[0] * 100, 2))+'%'

    return {'similar_score': preds_score}
