#FROM debian:latest AS env
#...
#RUN echo 'deb http://deb.debian.org/debian testing main' >> /etc/apt/so#urces.list
#RUN apt update -y
#RUN apt install -y gcc

FROM continuumio/miniconda3:latest

WORKDIR /the-shortest-url-1-rtfmbp
ADD . /the-shortest-url-1-rtfmbp
RUN conda env create -f environment.yml
SHELL ["conda", "run", "-n", "finncode", "/bin/bash", "-c"]
RUN echo "Make sure flask is installed:"
RUN python -c "import flask"
EXPOSE 5000
# The code to run when container is started:
ENTRYPOINT ["conda", "run", "-n", "finncode", "python", "src/tinyurl.py"]




