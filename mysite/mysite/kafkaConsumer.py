# importing the required modules  
from json import loads  
from kafka import KafkaConsumer  
# from pymongo import MongoClient


# generating the Kafka Consumer  
my_consumer = KafkaConsumer(
    'testnum',  
     bootstrap_servers = ['localhost : 9092'],  
     auto_offset_reset = 'earliest',  
     enable_auto_commit = True,  
     group_id = 'my-group',  
     value_deserializer = lambda x : loads(x.decode('utf-8'))  
     )


consumer_destination = []

for message in my_consumer:  
    message = message.value  
    consumer_destination.append(message)  
    print(message + " added to [consumer_destination]: " + consumer_destination)