FROM python:3.12-buster

ENV PYTHONUNBUFFERED 1
ENV LANG C.UTF-8
ENV TZ Asia/Tokyo

WORKDIR /backend
COPY ./backend/requirements.txt .
RUN pip install --upgrade pip \
    && pip install --upgrade setuptools \
    && pip install -r requirements.txt

COPY ./backend .

CMD ["bash", "-c", "uvicorn main:app --reload --host=0.0.0.0 --port=8000"]
# CMD ["gunicorn", "main:app", "-w", "4", "-t", "2", "-k", "uvicorn.workers.UvicornWorker", "-b", "0.0.0.0:8000"]