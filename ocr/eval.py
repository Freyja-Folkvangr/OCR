from urllib.request import Request, urlopen

from tqdm import tqdm
import numpy as np
import cv2
import keras.backend as K
from .settings import *

from .utils import pad_image, resize_image, create_result_subdir
from .tf_models import CRNN_STN


def set_gpus():
    os.environ["CUDA_VISIBLE_DEVICES"] = str([0, 1, 2, 3])[1:-1]


def create_output_directory():
    os.makedirs('eval', exist_ok=True)
    output_subdir = create_result_subdir('eval')
    print('Output directory: ' + output_subdir)
    return output_subdir



def load_image(img_path):
    if NB_CHANNELS == 1:
        return cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    else:
        return cv2.imread(img_path)


def load_image_from_url(url):
    # download the image, convert it to a NumPy array, and then read
    # it into OpenCV format

    # TODO resize the image according to https://blog.roboflow.com/you-might-be-resizing-your-images-incorrectly/
    # Ref. https://journalofbigdata.springeropen.com/articles/10.1186/s40537-019-0263-7

    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    resp = urlopen(req)
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_GRAYSCALE)

    return image


def preprocess_image(img):
    if img.shape[1] / img.shape[0] < 6.4:
        img = pad_image(img, (WIDTH, HEIGHT), NB_CHANNELS)
    else:
        img = resize_image(img, (WIDTH, HEIGHT))
    if NB_CHANNELS == 1:
        img = img.transpose([1, 0])
    else:
        img = img.transpose([1, 0, 2])
    img = np.flip(img, 1)
    img = img / 255.0
    if NB_CHANNELS == 1:
        img = img[:, :, np.newaxis]
    return img


def predict_text(model, img):
    y_pred = model.predict(img[np.newaxis, :, :, :])
    shape = y_pred[:, 2:, :].shape
    ctc_decode = K.ctc_decode(y_pred[:, 2:, :], input_length=np.ones(shape[0]) * shape[1])[0][0]
    ctc_out = K.get_value(ctc_decode)[:, :LABEL_LEN]
    result_str = ''.join([CHARACTERS[c] for c in ctc_out[0]])
    result_str = result_str.replace('-', '')
    return result_str


def evaluate(url: str):
    _, model = CRNN_STN()
    model.load_weights(MODEL_PATH)

    img = load_image_from_url(url)
    img = preprocess_image(img)
    result = predict_text(model, img)
    print('Detected result: {}'.format(result))
    return result


def evaluate_batch(model, data, output_subdir):
    for filepath in tqdm(data):
        img = load_image(filepath)
        img = preprocess_image(img)
        result = predict_text(model, img)
        output_file = os.path.basename(filepath)
        output_file = output_file[:-4] + '.txt'
        with open(os.path.join(output_subdir, output_file), 'w') as f:
            f.write(result)


