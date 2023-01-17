FROM ubuntu:latest 
ADD ./src /app
WORKDIR /app 

RUN apt-get -y install python3 
RUN apt-get -y install python3-pip

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["bash", "notebook/app_final.sh"]


