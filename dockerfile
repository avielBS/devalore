FROM python:3.7-alpine
WORKDIR /code
ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000

RUN python -m pip install flake8
RUN docker run -v $(pwd)/src:/src myimage flake8 src

COPY . .
CMD ["flask", "run"]
