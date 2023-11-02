import quixstreams as qx
import time
import datetime
import os
import json

# Quix injects credentials automatically to the client. 
# Alternatively, you can always pass an SDK token manually as an argument.
client = qx.QuixStreamingClient()

topics = os.environ["topics"]
topic_names = []
for topic in topics:
    print(str(topic))


# # Open the output topic where to write data out
# topic_producer = client.get_topic_producer(topic_id_or_name = os.environ["output"])

# # Set stream ID or leave parameters empty to get stream ID generated.
# stream = topic_producer.create_stream()
# stream.properties.name = "StatGenerator Stream"

# # Add metadata about time series data you are about to send. 
# stream.timeseries.add_definition(topic_name).set_range(-1.2, 1.2)
# stream.timeseries.buffer.time_span_in_milliseconds = 100

# totalGeneratorTime = 30000;
# print("Sending values for " + str(totalGeneratorTime / 100) + " seconds.")

# for index in range(0, totalGeneratorTime):
#             # .add_value("ParameterA", math.sin(index / 200.0) + math.sin(index) / 5.0) \

#     stream.timeseries \
#         .buffer \
#         .add_timestamp(datetime.datetime.utcnow()) \
#         .add_value(topic_name, 1) \
#         .publish()
#     time.sleep(0.01)

# print("Closing stream")
# stream.close()