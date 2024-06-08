FROM python:3.10
WORKDIR /back-end
COPY . /back-end
RUN apt-get update
RUN pip install --upgrade pip && \
    pip install -r requirements.txt
EXPOSE 5000
ENV FLASK_APP=app.py
CMD [ "python3", "-m", "flask","run", "--host=0.0.0.0" ]