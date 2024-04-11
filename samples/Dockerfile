FROM python:3.11.2

ENV TZ=Europe/Moscow

ARG SAMPLE_PATH
COPY ./${SAMPLE_PATH}/main.py loading/
COPY ./requirements.txt loading/
WORKDIR loading
RUN pip install -r requirements.txt

CMD ["python", "-u", "main.py"]