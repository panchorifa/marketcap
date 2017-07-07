"""
RequestMock
"""
class RequestMock(object):
    def __init__(self, urls):
        """
        Expects a dictionary of urls
        ie: { 'http://simon.com' : 'test/samples/simon.html'}
        """
        self.urls = urls


    def get(self, url):
        return open(self.urls[url], 'r').read()
