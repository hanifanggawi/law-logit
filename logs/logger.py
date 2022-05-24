import logging
from logstash_async.handler import AsynchronousLogstashHandler
from logstash_async.handler import LogstashFormatter

# Create the logger and set it's logging level
logger = logging.getLogger("logstash")
logger.setLevel(logging.DEBUG)        

# Create the handler
handler = AsynchronousLogstashHandler(
    host='48f84399-098a-4908-95b6-7dfb39b1e0b7-ls.logit.io', 
    port=30714, 
    ssl_enable=False, 
    ssl_verify=False,
    database_path='')
# Here you can specify additional formatting on your log record/message
formatter = LogstashFormatter()
handler.setFormatter(formatter)

# Assign handler to the logger
logger.addHandler(handler)