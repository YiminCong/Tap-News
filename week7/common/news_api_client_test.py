import news_api_client as client

def test_basic():
    news = client.getNewsFromSource()
    assert len(news) > 0
    news = client.getNewsFromSource(sources=['cnn'], sortBy='top')
    assert len(news) > 0

if __name__ == "__main__":
    test_basic()