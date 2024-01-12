FROM python:3.10

WORKDIR /webx

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .
RUN chmod 777 start.sh
CMD ["bash", "start.sh"]
