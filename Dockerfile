FROM ubuntu:latest

RUN apt update
RUN apt install python3 -y \
&& apt install python3-pip -y \
&& apt install python3-pytest -y 

COPY . ./demoTest

ENTRYPOINT [ "/demoTest/entrypointfile.sh" ]