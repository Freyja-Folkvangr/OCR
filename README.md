# OCR

## Prerequirements

1. Docker
2. Conda (For local virtual environment only)

## Build and run the container

The build will `COPY . /usr/src/app`, `RUN pip install`, `EXPOSE 8000`, and set the default command to `python manage.py runserver`.

You can then build and run the Docker image:

`docker build -t deep .`

`docker run --name some-django-app -d deep`

You can test it by visiting `http://container-ip:8000` in a browser or, if you need access outside the host, on `http://localhost:8000` with the following command:

`docker run --name some-django-app -p 8000:8000 -d deep`

## Local environment setup

1. Create a Conda environment

`conda create -n deep-ocr python=3.6`

`conda activate deep-ocr`

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
  ocr(url: "https://www.plot.cl/wp-content/uploads/2016/07/PARE.jpg")
}
``

