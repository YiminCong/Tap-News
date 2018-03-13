"""serivce backend"""
import os
import sys
from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer
import operations
sys.path.append(os.path.join(os.path.dirname(__file__), "utils"))
# import mongodb_client # pylint: disable=import-error, wrong-import-position

SERVER_HOST = 'localhost'
SERVER_PORT = 4040

def add(num1, num2):
    """Test"""
    return num1 + num2

def get_one_news():
    """getonenews"""
    # news = mongodb_client.get_db()['news'].find_one()
    return operations.getOneNews()

def get_news_summaries_for_user(user_id, page_num):
    """getNewsSummariesForUser"""
    return operations.getNewsSummariesForUser(user_id, page_num)

def log_news_click_for_user(user_id, news_id):
    """logNewsClickForUser"""
    print("log_news_click_for_user is called with %s and %s" % (user_id, news_id))
    operations.logNewsClickForUser(user_id, news_id)

RPC_SERVER = SimpleJSONRPCServer((SERVER_HOST, SERVER_PORT))
RPC_SERVER.register_function(add, 'add')
RPC_SERVER.register_function(get_one_news, 'get_one_news')
RPC_SERVER.register_function(get_news_summaries_for_user, 'getNewsSummariesForUser')
RPC_SERVER.register_function(log_news_click_for_user, 'logNewsClickForUser')
RPC_SERVER.serve_forever()
