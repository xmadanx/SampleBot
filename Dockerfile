COPY requirements.txt /requirements.txt
RUN cd /
RUN pip3 install -U pip && pip3 install -U -r requirements.txt
RUN mkdir /SampleBot
WORKDIR /SampleBot
COPY start.sh /start.sh
CMD ["/bin/bash", "/start.sh"]