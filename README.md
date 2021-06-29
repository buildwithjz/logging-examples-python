# Python logging examples

## About

Sample programs that just log "Hello World" in different formats:

* Native python logger format (non JSON)
* JSON format
* Elastic Common Schema JSON format

The point is to to have a set of docker images that can be used to test out log forwarding/shipping as well as transformation.

## Native logging example

This comes from just using the standard logging library in Python

## Json log example

This comes from this article: https://blog.sneawo.com/blog/2017/07/28/json-logging-in-python/ and just uses the "structlog" and "python-json-logger" libraries

## ECS Json example

The script logger-nonjson-to-ecs.py writes string/non-json log messages (Same string message as the Native logging example) into the Elastic Common Schema JSON format (under the message key), and inserts tags and labels into the log output.

This example uses the "ecs_logging" module:

* https://github.com/elastic/ecs-logging-python
* https://pypi.org/project/ecs-logging/
