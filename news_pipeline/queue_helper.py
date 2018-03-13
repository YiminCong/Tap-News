"""clear queue"""
import os
import sys

# import common package in parent directory
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))

from cloudAMQP_client import CloudAMQPClient

SCRAPE_NEWS_TASK_QUEUE_URL = "amqp://zzccaypk:iy5nHlQMyvqvt7e46xqHLZ8WeJrF_R-h@porpoise.rmq.cloudamqp.com/zzccaypk"
SCRAPE_NEWS_TASK_QUEUE_NAME = "tmp1"

DEDUPE_NEWS_TASK_QUEUE_URL = "amqp://hsebgbga:ODPWzuu-WcPTGQo8zGgRgZ16ZkoHwtSU@termite.rmq.cloudamqp.com/hsebgbga"
DEDUPE_NEWS_TASK_QUEUE_NAME = "tmp"

def clear_queue(queue_url, queue_name):
    """clear queue"""
    scrape_news_queue_client = CloudAMQPClient(queue_url, queue_name)

    num_of_messages = 0

    while True:
        if scrape_news_queue_client is not None:
            msg = scrape_news_queue_client.getMessage()
            if msg is None:
                # print("Cleared %d messages." % num_of_messages)
                return
            num_of_messages += 1

if __name__ == "__main__":
    clear_queue(SCRAPE_NEWS_TASK_QUEUE_URL, SCRAPE_NEWS_TASK_QUEUE_NAME)
    clear_queue(DEDUPE_NEWS_TASK_QUEUE_URL, DEDUPE_NEWS_TASK_QUEUE_NAME)
