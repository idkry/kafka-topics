#!/usr/bin/env python

import os
from kafka.admin import KafkaAdminClient, NewTopic
from kafka.errors import TopicAlreadyExistsError
import yaml

bootstrap_servers = os.environ.get('BOOTSTRAP_SERVERS')
client_id = os.path.basename(__file__)

topics_list = []
with open('topics.yml', 'r') as stream:
    try:
        topics = yaml.safe_load(stream)
        for t in topics:
            topics_list.append(NewTopic(name=t['topic'],
                                        num_partitions=t['partitions'],
                                        replication_factor=t['replication_factor'],
                                        topic_configs=t['config']))
        
    except yaml.YAMLError as ex:
        print(ex)

client = KafkaAdminClient(bootstrap_servers=bootstrap_servers, client_id=client_id)
try:
    client.create_topics(topics_list)
except TopicAlreadyExistsError as ex:
    pass
