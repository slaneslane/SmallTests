# tokenizedURL.py

class TokenizedURL(object):

    def __init__(self, base_uri, uid):
        self.base_uri = base_uri
        self.uid = uid
        self.__tokenized_uri = self.__compose_tokenized_uri()
        self.__tokenized_url = self.__compose_tokenized_url()

    def __compose_tokenized_uri(self):
        return 'login' + '?token=' + str(self.uid)

    def __compose_tokenized_url(self):
        return self.base_uri + self.__tokenized_uri

    def get_tokenized_URL(self):
        return self.__tokenized_url

base_uri = 'http://sond1974.nazwa.pl/accounts/'
uid = '30767d04-e9cd-4a74-becc-1301e38587c6'

url = TokenizedURL(base_uri, uid)
print(url.get_tokenized_URL())
