import quixstreams as qx
import time
import datetime
import os
import json
import random

# Quix injects credentials automatically to the client. 
# Alternatively, you can always pass an SDK token manually as an argument.
client = qx.QuixStreamingClient()

topics = json.loads(os.environ["topics"])

# Open the output topic where to write data out
topic_producer = client.get_topic_producer(topic_id_or_name = os.environ["output"])

# Set stream ID or leave parameters empty to get stream ID generated.
stream = topic_producer.create_stream()
stream.properties.name = "StatGenerator Stream"

# Add metadata about time series data you are about to send. 

for topic in topics:
    stream.timeseries.add_definition(topic["topic_name"]).set_range(topic["topic_minimum"], topic["topic_maximum"])
    stream.timeseries.buffer.time_span_in_milliseconds = 100


totalGeneratorTime = 30000;
print("Sending values for " + str(totalGeneratorTime / 100) + " seconds.")

for index in range(0, totalGeneratorTime):
    utc_now = datetime.datetime.utcnow()
    
    for topic in topics:
        stream.timeseries.buffer \
            .add_timestamp(utc_now) \
            .add_value(topic["topic_name"], random.randrange(topic["topic_minimum"], topic["topic_maximum"])) \
            .publish()

    time.sleep(0.25)

print("Closing stream")
stream.close()