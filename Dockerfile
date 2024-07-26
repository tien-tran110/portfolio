FROM quay.io/centos/centos:stream9

RUN dnf install -y python 3.9

WORKDIR /myportfolio

COPY . .

RUN pip3 install -r requirements.txt

CMD ["flask", "run", "--host=0.0.0.0"]

EXPOSE 5000