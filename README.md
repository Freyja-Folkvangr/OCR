# OCR

## Prerequirements

1. Conda

## Local environment setup

1. Create a Conda environment

`conda create -n deeplegal-ocr python=3.6`

`conda activate deeplegal-ocr`

`pip install -r requirements.txt`

## Run Flask

`export FLASK_APP=flaskr`

`export FLASK_ENV=development`

`flask run`

## Limitations

It is supported to evaluate one image from url at a time.