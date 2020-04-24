FROM python:3

ADD bot.py /
ADD command_list.yaml /
ADD requirements.txt /

RUN pip install -r requirements.txt

CMD [ "python", "./bot.py"]