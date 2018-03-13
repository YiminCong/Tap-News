from cloudAMQP_client import CloudAMQPClient

# CLOUDAMQP_URL2 = "amqp://zzccaypk:iy5nHlQMyvqvt7e46xqHLZ8WeJrF_R-h@porpoise.rmq.cloudamqp.com/zzccaypk"
CLOUDAMQP_URL = "amqp://hsebgbga:ODPWzuu-WcPTGQo8zGgRgZ16ZkoHwtSU@termite.rmq.cloudamqp.com/hsebgbga"
TEST_QUEUE_NAME = "test"

def test_basic():
    client = CloudAMQPClient(CLOUDAMQP_URL, TEST_QUEUE_NAME)

    sentMsg = {"test":"test"}
    client.sendMessage(sentMsg)
    receivedMsg = client.getMessage()

    assert sentMsg == receivedMsg
    print("test_basic passed!")

if __name__ == "__main__":
    test_basic()