import string, os

# TODO These settings can be static or being parametrized depending of the height or width


CHARACTERS = '0123456789' + string.ascii_lowercase + '-'
DATA_PATH = 'test'

module_dir = os.path.dirname(__file__)  # get current directory
MODEL_PATH = os.path.join(module_dir, 'ocr_model.hdf5')

WIDTH = 200
HEIGHT = 31
LABEL_LEN = 16
NB_CHANNELS = 1
MODEL = 'CRNN_STN'
CONV_FILTER_SIZE = [64, 128, 256, 256, 512, 512, 512]
LSTM_NB_UNITS = [128, 128]
TIMESTEPS = 50
DROPOUT_RATE = 0.25