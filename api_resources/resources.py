from api_resources.check_controller import CheckController


class Resource(object):
    _cls = None
    _url = None

    def __init__(self, cls, url):
        self._cls = cls
        self._url = url

    def get_cls(self):
        return self._cls

    def get_url(self):
        return self._url


resources = [
    Resource(CheckController, "check")
]
