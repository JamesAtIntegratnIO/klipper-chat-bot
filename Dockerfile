FROM python:3
ADD requirements.txt /
RUN pip install -r requirements.txt

ADD kevin/ /
ADD kevin/command_list.yaml /


CMD [ "python", "kevin.py"]