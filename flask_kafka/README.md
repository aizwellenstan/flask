Video Streaming System with Kafka and Python
===

## Installation

```sh
$ brew install kafka
```

```sh
$ python -m venv --without-pip venv # https://stackoverflow.com/a/26314477
$ . venv/bin/activate
$ curl https://bootstrap.pypa.io/get-pip.py | python
$ deactivate
$ . venv/bin/activate
$ pip install -r requirements.txt
```

## Usage

Kafka:

```sh
$ brew services start zookeeper
$ brew services start kafka # on port 9092
```

Producer:

```sh
$ python src/producer.py resources/awesome_video.mp4
```

Consumer:

```sh
$ python src/consumer.py
```