# OCR

## Prerequirements

1. Docker
2. Conda (For local virtual environment only)

## Build the container

`docker build .`

## Local environment setup

1. Create a Conda environment

`conda create -n deeplegal-ocr python=3.6`

`conda activate deeplegal-ocr`

`pip install -r requirements.txt`

Optional step: `python manage.py migrate`

## Run the project

`python manage.py runserver 0.0.0.0:8000`

## Testing

1. Open `127.0.0.1:8000/graphql`
2. Perform a query

### Sugested query
``
{
  ocr(url: "")
}
``

