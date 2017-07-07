"""
RequestMock
"""
class ResponseMock(object):
    def __init__(self, text):
        self.text = text

class RequestMock(object):
    def __init__(self, urls):
        """
        Expects a dictionary of urls
        ie: { 'http://simon.com' : 'test/samples/simon.html'}
        """
        self.urls = urls


    def get(self, url):
        text = open(self.urls[url], 'r').read()
        return ResponseMock(text)
