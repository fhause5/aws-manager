FROM python:3.7
WORKDIR /app
COPY setup.py /app
COPY aws_python /app

RUN pip install pipenv && \
    pip3.7 install --user -U pipenv && \
    pipenv shell && \
    pip install -e .

#CMD ['aws_python', '----help']
