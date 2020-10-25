FROM tiangolo/meinheld-gunicorn:python3.8

COPY ./wordlist /app/wordlist
COPY requirements.txt /app
COPY main.py /app
RUN python -m pip install --upgrade pip &&\ 
    pip install -r requirements.txt
