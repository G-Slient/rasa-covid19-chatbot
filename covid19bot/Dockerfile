FROM ubuntu:18.04
ENTRYPOINT []
RUN apt-get update && apt-get install -y python3 python3-pip && python3 -m pip install --no-cache --upgrade pip && pip3 install --no-cache rasa==1.9.6
ADD . /covid19bot/
RUN chmod +x /covid19bot/start_services.sh
CMD /covid19bot/start_services.sh