FROM python:3.9

ENV LANG='en_US.UTF-8' LANGUAGE='en_US.UTF-8' LC_ALL='en_US.UTF-8'

RUN apt-get update -y && \
    apt-get install -y python3-pip python-dev && \
    apt-get install -y locales && \
    locale-gen en_US.UTF-8 && \
    pip install --upgrade pip

RUN apt-get -y update && apt-get install -y --no-install-recommends \
         ca-certificates \
         build-essential \
         curl &&\
         rm -rf /var/lib/apt/lists/*

RUN apt-get clean

RUN pip install flask gevent gunicorn && \
        rm -rf /root/.cache

COPY requirements.txt .
RUN pip install -r requirements.txt

ENV PYTHON_VERSION=3.9
ENV PYTHONUNBUFFERED=TRUE
ENV PYTHONDONTWRITEBYTECODE=TRUE
ENV PATH="/opt/program:${PATH}"

# Set up the program in the image
COPY predictor /opt/program

RUN chmod 755 /opt/program
WORKDIR /opt/program
CMD ["python3", "predictor.py"]
