import os


class Config(object):
    DEBUG = False
    HOST = '127.0.0.1'  #0.0.0.0则非本机也可以访问
    PORT = '5500'
    SECRET_KEY = 'redsfsfsfsfis'
    SIAMESE_MODEL_FILE = os.path.abspath(os.path.join(os.path.curdir, "data//model//Model.hdf5"))


class Development(Config):
    DEBUG = True


class Production(Config):
    DEBUG = False


VALIDATION_SPLIT = 0.2
RATE_DROP_LSTM = 0.17
RATE_DROP_DENSE = 0.25
NUMBER_LSTM = 50
NUMBER_DENSE_UNITS = 50
ACTIVATION_FUNCTION = 'relu'

MIN_FREQUENT = 5  #最低词频
MAX_DOCUMENT_LENGTH = 400   #文件长
VOCABULARY_DIM = 256    #词向量维数
BATCH_SIZE = 72
NUM_EPOCH = 200
WINDOW_SIZE = 8  # 窗口大小
N_ITERATIONS = 5  # 迭代次数，默认为5 #定义词向量模型
DATA_DIR = os.path.abspath(os.path.join(os.path.curdir, "data"))


siamese_config = {
    'MAX_DOCUMENT_LENGTH': MAX_DOCUMENT_LENGTH,
    'VALIDATION_SPLIT': VALIDATION_SPLIT,
    'RATE_DROP_LSTM': RATE_DROP_LSTM,
    'RATE_DROP_DENSE': RATE_DROP_DENSE,
    'NUMBER_LSTM': NUMBER_LSTM,
    'NUMBER_DENSE_UNITS': NUMBER_DENSE_UNITS,
    'ACTIVATION_FUNCTION': ACTIVATION_FUNCTION,

    'MIN_FREQUENT': MIN_FREQUENT,
    'VOCABULARY_DIM': VOCABULARY_DIM,
    'BATCH_SIZE': BATCH_SIZE,
    'NUM_EPOCH': NUM_EPOCH,
    'WINDOW_SIZE': WINDOW_SIZE,
    'N_ITERATIONS': N_ITERATIONS,
    'DATA_DIR': DATA_DIR,
}
