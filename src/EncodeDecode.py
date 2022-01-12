import random, string


class EncodeDecode:
    def __init__(self):
        """
        initialize data store object
        """
        self.encodemap = {}
        self.decodemap = {}
        self.base_url = "http://127.0.0.1:5000/"
        self.base62 = string.digits + string.ascii_letters

    def encode(self, longurl) -> str:

        """ encodes a long URL into short url """

        if longurl not in self.encodemap:
            shorturl = "".join(
                random.SystemRandom().choice(self.base62) for _ in range(6)
            )
            self.encodemap[longurl] = shorturl
            self.decodemap[shorturl] = longurl
        return self.base_url + self.encodemap[longurl]

    def decode(self, shorturl) -> str:
        """ decodes a short URL into a long url """

        return self.decodemap[shorturl]
