import os
import sys

# from newspaper import Article

# import common package in parent directory
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'scrapers'))

import cnn_news_scraper # pylint: disable=import-error, wrong-import-position
from cloudAMQP_client import CloudAMQPClient # pylint: disable=import-error, wrong-import-position

DEDUPE_NEWS_TASK_QUEUE_URL = "amqp://hsebgbga:ODPWzuu-WcPTGQo8zGgRgZ16ZkoHwtSU@termite.rmq.cloudamqp.com/hsebgbga"
DEDUPE_NEWS_TASK_QUEUE_NAME = "tmp"
SCRAPE_NEWS_TASK_QUEUE_URL = "amqp://zzccaypk:iy5nHlQMyvqvt7e46xqHLZ8WeJrF_R-h@porpoise.rmq.cloudamqp.com/zzccaypk"
SCRAPE_NEWS_TASK_QUEUE_NAME = "tmp1"

SLEEP_TIME_IN_SECONDS = 5

dedupe_news_queue_client = CloudAMQPClient(DEDUPE_NEWS_TASK_QUEUE_URL, DEDUPE_NEWS_TASK_QUEUE_NAME)
scrape_news_queue_client = CloudAMQPClient(SCRAPE_NEWS_TASK_QUEUE_URL, SCRAPE_NEWS_TASK_QUEUE_NAME)


def handle_message(msg):
    if msg is None or not isinstance(msg, dict):
        return

    task = msg
    text = None

    if task['source'] == 'cnn':
        text = cnn_news_scraper.extractNews(task['url'])
    # else:
    #     print task['source']

    task['text'] = text

    dedupe_news_queue_client.sendMessage(task)

while True:
    if scrape_news_queue_client is not None:
        msg = scrape_news_queue_client.getMessage()
        if msg is not None:
            # Parse and process the task
            try:
                handle_message(msg)
            except Exception as e:
                # print(e)
                pass
        scrape_news_queue_client.sleep(SLEEP_TIME_IN_SECONDS)