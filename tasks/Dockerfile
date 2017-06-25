FROM python:3.6

ENV NAME flask_app

RUN mkdir -p /opt/$NAME
COPY requirements.txt /opt/$NAME/requirements.txt
RUN cd /opt/$NAME && pip install -r requirements.txt
COPY app/ /opt/$NAME/app/
COPY entrypoint.sh /opt/$NAME/entrypoint.sh

RUN mkdir -p /opt/$NAME/data
# COPY data/ /opt/$NAME/data/

# Tell Docker we are going to use this port
EXPOSE 7878

# Copy the application folder inside the container
WORKDIR /opt/$NAME


ENTRYPOINT ["./entrypoint.sh"]