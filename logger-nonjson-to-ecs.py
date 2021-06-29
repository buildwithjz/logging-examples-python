# Example: https://www.elastic.co/guide/en/ecs-logging/python/current/installation.html

import logging
import time
import ecs_logging

logger = logging.getLogger("app")
logger.setLevel(logging.DEBUG)

# Add an ECS formatter to the Handler
handler = logging.StreamHandler()
handler.setFormatter(ecs_logging.StdlibFormatter())
logger.addHandler(handler)

while(True):
    logger.debug("Hello World!", extra={"tags":["test_tag"],"labels":{"test_label_key":"test_label_value"}})
    time.sleep(1)
