# Pull base image.
FROM jupyter/scipy-notebook
MAINTAINER xx

# get curl
USER root
RUN apt-get upgrade; apt-get update; apt-get install -y curl

# set user (the one from scipy-notebook base image)
USER jovyan

# default pip is python 3!
RUN pip install https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.10.0-cp35-cp35m-linux_x86_64.whl

# add Live (reveal) slideshows
RUN wget https://github.com/pdonorio/RISE/archive/master.tar.gz \
    && tar xvzf *.gz && cd *master && python3 setup.py install

RUN pip install runipy
ENV KERAS_BACKEND tensorflow
RUN pip install keras

RUN pip install ipdb

WORKDIR /data
EXPOSE 8888
CMD jupyter notebook --no-browser --ip=0.0.0.0
