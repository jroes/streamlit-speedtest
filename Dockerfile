FROM python:3.7
EXPOSE 8501
WORKDIR /app
COPY . .
RUN pip3 install -r requirements.txt