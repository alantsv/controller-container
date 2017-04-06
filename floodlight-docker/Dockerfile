FROM java:9

MAINTAINER Alan Veloso <alantsv@gmail.com>

RUN apt-get update && apt-get -y install git && apt-get -y install && apt-get -y install build-essential ant maven python-dev

RUN git clone git://github.com/floodlight/floodlight.git

WORKDIR /floodlight

RUN git submodule init

RUN git submodule update

RUN ant

RUN mkdir /var/lib/floodlight

RUN chmod 777 /var/lib/floodlight

CMD /usr/bin/java -jar target/floodlight.jar
