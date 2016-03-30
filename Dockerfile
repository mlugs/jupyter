# Pull base image.
FROM jupyter/scipy-notebook
MAINTAINER xx

# get curl
USER root
RUN apt-get upgrade; apt-get update; apt-get install -y curl

# set user (the one from scipy-notebook base image)
USER jovyan

# default pip is python 3!
RUN curl https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.7.1-cp34-none-linux_x86_64.whl > /tmp/tensorflow-0.7.1-cp35-none-linux_x86_64.whl
RUN pip install /tmp/tensorflow-0.7.1-cp35-none-linux_x86_64.whl
RUN pip install skflow

# add Live (reveal) slideshows
RUN wget https://github.com/pdonorio/RISE/archive/master.tar.gz \
    && tar xvzf *.gz && cd *master && python3 setup.py install

WORKDIR /data
EXPOSE 8888
CMD jupyter notebook --no-browser --ip=0.0.0.0
