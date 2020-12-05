FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /StockSim
WORKDIR /StockSim
ADD requirements.txt /StockSim/
RUN pip install --upgrade pip && pip install -r requirements.txt
ADD . /StockSim