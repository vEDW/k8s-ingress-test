# Alpine base image that contains python 3.7
FROM python:3.7-alpine
# define the directory to work in
WORKDIR /app

# copy the requirements.txt file to the work directory
#COPY requirements.txt .

# Copy rest of the source code
COPY . /app

# Install some system deps in a virtual environment named .build-deps, you can name it what ever you want
# install pip dependencies in the same layer
RUN apk add --no-cache --virtual .build-deps \
    build-base openssl-dev pkgconfig libffi-dev \
    cups-dev jpeg-dev && \
    pip install --no-cache-dir -r requirements.txt && \
    apk del .build-deps # delete the .build-deps in the same layer

# EXPOSE the needed ports, for example 8080
EXPOSE 5000
# Running Command or Entry Point
ENTRYPOINT [ "python" ]

CMD [ "ping.py" ]